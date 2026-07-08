import os
import io
from typing import Optional

import orjson
from requests.sessions import Session

from web.project.logger import logger
from web.project.celery import celery_app

import matplotlib.pyplot as plt


colors_default = {
    "broken": "#ffd050",
    "failed": "#fd5a3e",
    "passed": "#97cc64",
    "skipped": "#aaa",
    "unknown": "#d35ebe",
    "in_progress": "#7fa6d8"
}


def get_chart(
        stats: dict[str, int],
        title: Optional[str] = None
) -> io.BytesIO:
    labels = []
    values = []
    colors = []
    explode = []
    wedge_properties = {"edgecolor": "white", 'linewidth': 2}

    for k, v in filter(
            lambda x: x[0] != 'total' and x[1] != 0,
            stats.items()
    ):
        if v != 0:
            labels.append(k)
            values.append(v)
            colors.append(colors_default.get(k, "#111"))
            explode.append(round(v / (stats["total"] * 10), 4))

    fig1, ax1 = plt.subplots()
    patches, texts, pcts = ax1.pie(
        values, labels=labels, colors=colors, autopct='%1.2f%%',
        wedgeprops=wedge_properties, explode=explode,
        textprops={'size': 'x-large'}
    )
    for i, patch in enumerate(patches):
        texts[i].set_color(patch.get_facecolor())
    ax1.axis('equal')
    ax1.legend(loc='best')

    if title is not None:
        plt.title(title).set_color('white')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', transparent=True)
    buf.seek(0)
    return buf


@logger.catch
def send_report(
        launch_id: int,
        with_report: bool = False,
        with_chart: bool = False,
        chat_id: str = os.getenv("JENKINS_CHAT")
):
    with Session() as client:
        client.verify = False
        client.headers = {
            "Authorization": "Api-Token {token}".format(
                token=os.getenv("ALLURE_TOKEN")
            ),
        }
        # response = client.post(
        #     f'{os.getenv("ALLURE_ENDPOINT")}/api/rs/launch/{launch_id}/close')
        # response.raise_for_status()

        if with_report:
            response = client.get(
                f'{os.getenv("ALLURE_ENDPOINT")}/api/rs/launch/{launch_id}')
            response.raise_for_status()
            launch_info_json = response.json()

            response = client.get(
                f'{os.getenv("ALLURE_ENDPOINT")}'
                f'/api/rs/launch/{launch_id}/statistic')
            response.raise_for_status()
            launch_stats_json = response.json()

            response = client.get(
                f'{os.getenv("ALLURE_ENDPOINT")}'
                f'/api/rs/launch/{launch_id}/unresolved',
                params={
                    'size': 1500
                }
            )
            response.raise_for_status()
            unresolved_json = response.json()

    if with_report:
        stats = {
            "launch_id": launch_id,
            "stats": {},
            "name": launch_info_json["name"],
            "tags": [
                tag["name"] for tag in launch_info_json.get("tags", [])
            ],
            "branch": tuple(
                filter(
                    lambda x: x["name"] in ("master", "release") or x[
                        "name"].startswith("IM"),
                    launch_info_json.get("tags", []) or [{"name": "master"}]
                )
            )[-1]["name"]
        }

        total = 0
        for key in (
                'broken', 'failed', 'passed', 'skipped',
                'in_progress', 'unknown',
                'total'
        ):
            stats["stats"].setdefault(key, 0)
        for stat in launch_stats_json:
            stats["stats"][stat.get("status", "in_progress")] = stat[
                "count"]
            total += stat["count"]
        stats["stats"]["total"] = total

        failed_tests = []
        for test in filter(
                lambda x: x["status"] == "failed",
                unresolved_json["content"]
        ):
            failed_tests.append(
                {
                    "testCaseId": test["testCaseId"],
                    "name": test["name"],
                    "link": f"{os.getenv('ALLURE_ENDPOINT')}/testresult/{test['id']}"
                }
            )
        stats["failed"] = failed_tests
        broken_tests = []
        for test in filter(
                lambda x: x["status"] == "broken",
                unresolved_json["content"]
        ):
            broken_tests.append(
                {
                    "testCaseId": test["testCaseId"],
                    "name": test["name"],
                    "link": f"{os.getenv('ALLURE_ENDPOINT')}/testresult/{test['id']}"
                }
            )
        stats["broken"] = broken_tests

        if stats["stats"]["failed"] != 0 or stats["stats"]["broken"] != 0:
            text = """<code>❌ <a href=\"{launch_link}\">{name}</a>
Какие-то ошибки в UI тестах

Успешно          (passed): {passed}
Пропущено       (skipped): {skipped}
Неуспешно        (failed): {failed}
Ошибки           (broken): {broken}
В процессе  (in progress): {in_progress}
Неизвестно      (unknown): {unknown}
Всего             (total): {total}</code>
    
    """.format(
                name=stats["name"],
                launch_link=
                os.getenv("ALLURE_ENDPOINT") + f"launch/{stats['launch_id']}",
                **stats["stats"]
            )
            if 0 < stats["stats"]["broken"] < 20:
                text += "⚠️ Какие-то ошибки:\n"
                for test in stats["broken"]:
                    text += "#{testCaseId} <a href=\"{link}\">{name}</a>\n".format(
                        **test
                    )
                text += "\n"
            if 0 < stats["stats"]["failed"] < 20:
                text += "❌ Некоторые UI тесты не пройдены:\n"
                for test in stats["failed"]:
                    text += "#{testCaseId} <a href=\"{link}\">{name}</a>\n".format(
                        **test
                    )
                text += "\n"
        else:
            text = """<code>✅ <a href=\"{launch_link}\">{name}</a>
UI тесты прошли успешно

Успешно          (passed): {passed}
Пропущено       (skipped): {skipped}
Неуспешно        (failed): {failed}
Ошибки           (broken): {broken}
В процессе  (in progress): {in_progress}
Неизвестно      (unknown): {unknown}
Всего             (total): {total}</code>""".format(
                name=stats["name"],
                launch_link=f"{os.getenv('ALLURE_ENDPOINT')}/launch/{stats['launch_id']}",
                **stats["stats"]
            )
        with Session() as client:

            markup = [
                [{
                    "text": "Allure TestOps",
                    "url": f"{os.getenv('ALLURE_ENDPOINT')}"
                           f"/launch/{stats['launch_id']}",
                    "style": "attention"
                }]
            ]
            if stats["stats"]["broken"] + stats["stats"]["failed"] > 0:
                markup.append([{
                    "text": "Перезапустить упавшие тесты",
                    "callbackData": f"restart_launch|{stats['launch_id']}",
                    "style": "attention"
                }])

            client.verify = False
            logger.info("Sending report")
            if not with_chart:
                client.get(
                    f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendText',
                    params={
                        "token": os.getenv("BOT_TOKEN"),
                        "chatId": os.getenv("TRASH_CHAT"),
                        "text": text.strip(),
                        "parseMode": "HTML",
                        "inlineKeyboardMarkup": orjson.dumps(markup).decode()
                    })
            else:
                response = client.post(
                    f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendFile',
                    params={
                        "token": os.getenv("BOT_TOKEN"),
                        "chatId": chat_id,
                        "caption": text.strip(),
                        "parseMode": "HTML",
                        "inlineKeyboardMarkup": orjson.dumps(markup).decode()
                    },
                    files={'file': get_chart(stats["stats"], stats["name"])}
                )
                response.raise_for_status()
                logger.info(response.text)

    return stats


@celery_app.task(name='send_report')
def send_report_task(
        launch_id: int,
        with_report: bool = False,
        with_chart: bool = False,
        chat_id: str = os.getenv("JENKINS_CHAT")
):
    return send_report(launch_id, with_report, with_chart, chat_id)
