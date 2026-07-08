import json
import os
import time

from requests.sessions import Session

from celery.utils.log import get_task_logger

from jira import JIRA

from web.project.db import JiraEventTypeEnum
from web.project.jira_acc.constants import private_key

from web.project.celery import celery_app


logger = get_task_logger(__name__)


session = Session()
session.verify = False


jira_account = JIRA(
    options={
        "server": "https://jira.vk.team"
    },
    oauth={
        'access_token': '1FiifswDIuZPuRBlMZsGBI70qEOPmhkl',
        'access_token_secret': '5H0CX6PNzwrUFN4YHfDe8LC4Qz5W7ARX',
        'consumer_key': 'Oa3xK77mfYkg7oSz',
        'key_cert': private_key
    }
)


base_fields = ['priority', 'comment', 'issuetype']


fields_name_dict = {
    'customfield_74025': 'Product priority',
    'customfield_43212': 'Product priority -> Источник',
    'customfield_74014': 'Product priority -> Статус SLA',
    'customfield_74015': 'Product priority -> Public Alarm',
    'customfield_74023': 'Severity',
    'customfield_43707': 'Severity -> Функционал',
    'customfield_40808': 'Severity -> Влияние',
    'customfield_40809': 'Severity -> Массовость',
    'customfield_40810': 'Severity -> Сложность воспроизведения',
}


product_priority_fields = [
    'customfield_74025',
    'customfield_43212',
    'customfield_74014',
    'customfield_74015',
]


severity_fields = [
    'customfield_74023',
    'customfield_43707',
    'customfield_40808',
    'customfield_40809',
    'customfield_40810',
]


def fields_check(*args):
    for arg in args:
        assert arg, "Field is empty"


def get_priority_by_fields(fields):

    product_priority = fields['customfield_74025']
    severity = fields['customfield_74023']

    fields_check(
        *[
            value
            for key, value in fields.items()
            if key in product_priority_fields + severity_fields
        ]
    )

    if product_priority not in (
            'Блокирующий', 'Критический', 'Стандартный', 'Незначительный'):
        raise ValueError(f'Unknown product_priority value: {product_priority}')

    if severity not in (
            'Blocker', 'Critical', 'Major', 'Minor'):
        raise ValueError(f'Unknown severity value: {severity}')

    if (product_priority == 'Блокирующий' and severity == 'Blocker') or \
            (product_priority == 'Критический' and severity == 'Blocker') or \
            (product_priority == 'Блокирующий' and severity == 'Critical'):
        return 'Блокирующий', product_priority, severity
    elif (product_priority == 'Стандартный' and severity == 'Blocker') or \
            (product_priority == 'Критический' and severity == 'Critical') or \
            (product_priority == 'Блокирующий' and severity == 'Major'):
        return 'Критический', product_priority, severity
    elif (product_priority == 'Незначительный' and severity == 'Blocker') or \
            (product_priority == 'Стандартный' and severity == 'Critical') or \
            (product_priority == 'Критический' and severity == 'Major') or \
            (product_priority == 'Блокирующий' and severity == 'Minor') or \
            (product_priority == 'Незначительный' and severity == 'Critical') or \
            (product_priority == 'Стандартный' and severity == 'Major') or \
            (product_priority == 'Критический' and severity == 'Minor'):
        return 'Стандартный', product_priority, severity
    else:
        return 'Незначительный', product_priority, severity


@celery_app.task(name='IMSERVER_MAP_PRIORITY')
def imserver_map_priority(key: str):

    time.sleep(10)

    logger.info(f'Task key: {key}')

    issue = session.get(
        f'http://web:8000/api/v1/jira/task/{key}',
        params={
            'fields': ','.join(
                base_fields +
                product_priority_fields +
                severity_fields
            )
        }
    ).json().get('issue', {})

    if issue['fields']['issuetype']['subtask'] \
            or issue['fields']['issuetype']['name'] not in ["Bug", "Ошибка"]:

        logger.info(f"{key} - {issue['fields']['issuetype']['name']} ignoring")
        return

    comments = issue["fields"]["comment"]["comments"]
    product_priority, severity = None, None

    current_priority = issue["fields"]["priority"]["name"]

    try:
        mapped_task_priority, product_priority, severity = \
            get_priority_by_fields(
                issue["fields"]
            )
    except (ValueError, AssertionError) as error:
        logger.error(error)
        mapped_task_priority = None

    log_text = f'{key} | current priority - {current_priority} | ' \
        f'new priority - {mapped_task_priority}\n\n' + '\n'.join([
        f'{fields_name_dict[key]} = '
        f'{value["value"] if isinstance(value, dict) else value}'
        for key, value in issue['fields'].items()
        if key in fields_name_dict.keys()
    ])

    send_message(log_text)

    logger.info(log_text)
    if mapped_task_priority is not None \
            and current_priority != mapped_task_priority:
        try:
            jira_account.issue(key).update(
                fields={
                    'priority': {
                        'name': mapped_task_priority
                    }
                }
            )

        except Exception as error:
            logger.error(error)
            send_message(str(f'{type(error)}: {str(error)}'))
    elif mapped_task_priority is None:

        if not comments or comments[-1]["author"]["key"] != 'JIRAUSER88681':
            comment = \
                'Коллеги, пожалуйста, ' \
                'заполните следующие поля:\n' + '\n'.join([
                    fields_name_dict[key]
                    for key, value in issue['fields'].items()
                    if key in product_priority_fields + severity_fields
                    and value is None
                ])

            jira_account.add_comment(
                issue=key,
                body=comment
            )

        if 'v.korobov@mail.msk' not in map(
            lambda x: x.name, jira_account.watchers(issue=key).watchers
        ):
            jira_account.add_watcher(
                issue=key,
                watcher='v.korobov@mail.msk'
            )


def send_message(text: str):
    with Session() as client:
        client.post(
            f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendText',
            params={
                "token": os.getenv("BOT_TOKEN"),
                "chatId": os.getenv("JIRA_CHAT"),
                "text": text,
            }
        )


@celery_app.task(name='jira_send_report')
def send_report_task(row_id: int) -> tuple[int, str]:
    logger.info(f'ROWID: {row_id}')

    result = session.get(f'http://web:8000/api/v1/jira/task/hook/{row_id}')

    result.raise_for_status()

    logger.info(result)

    with Session() as client:
        response = client.post(
            f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendText',
            params={
                "token": os.getenv("BOT_TOKEN"),
                "chatId": os.getenv("JIRA_CHAT"),
                "text": f'<pre><code class="python">'
                        f'{result.text}'
                        f'</code></pre>',
                "parseMode": "HTML"
            }
        )
    return response.status_code, response.text

@celery_app.task(name='imsupport_critical_notify')
def imsupport_critical_notify(row_id: int):

    TO_NOTIFY = False

    hook = session.get(
        f'http://web:8000/api/v1/jira/task/hook/{row_id}'
    ).json()['hook']

    if hook['issue']['fields']['priority']['name'] not in (
        'Критический',
        'Critical',
        'Блокирующий',
        'Blocker'
    ) or hook['issue']['fields']['issuetype']['name'] not in (
        'Incident',
        'Report'
    ):
        return

    if hook['event_type'] in (
            JiraEventTypeEnum.JIRA_ISSUE_CREATED,
            JiraEventTypeEnum.ISSUE_CREATED,
    ):
        TO_NOTIFY = True

    if hook['event_type'] in (
            JiraEventTypeEnum.JIRA_ISSUE_UPDATED,
            JiraEventTypeEnum.ISSUE_UPDATED
    ):
        for item in filter(
            lambda x:
            x['field'] == 'priority'
            and x['toString'] in (
                'Критический',
                'Critical',
                'Блокирующий',
                'Blocker'
            ) and x['fromString'] not in (
                'Критический',
                'Critical',
                'Блокирующий',
                'Blocker'
            )
            ,
            hook['changelog']['items']
        ):
            TO_NOTIFY = True
            break

    if TO_NOTIFY:
        hook = hook['issue']
        text = '''🚩Появился критический инцидент:
[{issuetype}] <a href="https://jira.vk.team/browse/{issue_key}">{issue_key}</a> <b>{summary}</b>

Затронуты версии: {bugVersions}
Инсталляция: {installation}
Заказчик: {buyer}
Продукт: {product}
Клиент / Домен: {client_domain}
Платформа: {platform}

Описание:
{description}'''.format(
            issuetype=hook['fields']['issuetype']['name'],
            issue_key=hook['key'],
            summary=hook['fields']['summary'],
            installation=(hook['fields']['customfield_69400'] or {}).get('value'),
            buyer=(hook['fields']['customfield_73926'] or {}).get('value'),
            product=(hook['fields']['customfield_40112'] or {}).get('value'),
            description=hook['fields']['description'],
            bugVersions=', '.join(map(
                lambda x: x['name'].strip(),
                hook['fields'].get('versions', ['none']) or ['none']
            )),
            client_domain=','.join(
                hook['fields'].get('customfield_72814', ['none']) or ['none']
            ),
            platform=', '.join(map(
                lambda x: x['value'].strip(),
                hook['fields']['customfield_18216'])
            )
        )
        with Session() as client:
            client.get(
                url=f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendText',
                params={
                    'token': os.getenv('BOT_TOKEN'),
                    'chatId': 'AtDwEUtiaQtaWn0J',
                    'text': text,
                    'parseMode': 'HTML',
                    'inlineKeyboardMarkup': json.dumps([[
                        {
                            "text": hook['key'],
                            "url": 'https://jira.vk.team/browse/{}'.format(
                                hook['key']
                            ),
                            "style": "primary"
                        }
                    ]])
                }
            )


