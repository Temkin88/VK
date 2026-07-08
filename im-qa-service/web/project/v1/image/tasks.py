import io
import json
import os

from PIL.Image import Image
from requests.sessions import Session

from web.project.logger import logger

from web.project.celery import celery_app


@logger.catch(default=True)
def send_report_on_image_diff(
        node_name: str,
        BRANCH_NAME: str,
        test_case: str,
        screenshot_name: str,
        mean_sum: float,
        requested_mean_sum: float,
        diff: float,
        original_image_path: str,
        image_from_request_path: str,
        diff_image_path: str,
):
    logger.info('Started send_report_on_image_diff')
    logger.info(original_image_path)
    logger.info(image_from_request_path)
    logger.info(diff_image_path)

    with Session() as client:
        with open(original_image_path, 'rb') as f:
            original_image = io.BytesIO(f.read())
        original_image_file_id = client.post(
            url=f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendFile',
            params={
                'token': os.getenv('BOT_TOKEN'),
                'chatId': os.getenv('TRASH_CHAT')
            },
            files={'file': original_image}
        ).json()

        logger.info(original_image_file_id)
        original_image_file_id = original_image_file_id['fileId']

        with open(image_from_request_path, 'rb') as f:
            image_from_request = io.BytesIO(f.read())
        image_from_request_file_id = client.post(
            url=f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendFile',
            params={
                'token': os.getenv('BOT_TOKEN'),
                'chatId': os.getenv('TRASH_CHAT')
            },
            files={'file': image_from_request}
        ).json()

        logger.info(image_from_request_file_id)
        image_from_request_file_id = image_from_request_file_id['fileId']

        with open(diff_image_path, 'rb') as f:
            diff_image = io.BytesIO(f.read())
        diff_image_file_id = client.post(
            url=f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendFile',
            params={
                'token': os.getenv('BOT_TOKEN'),
                'chatId': os.getenv('TRASH_CHAT')
            },
            files={'file': diff_image}
        ).json()

        logger.info(diff_image_file_id)
        diff_image_file_id = diff_image_file_id['fileId']

        text = f"""Node Name: {node_name}
Branch: {BRANCH_NAME}

Тест-кейс: {test_case}
Сравниваемый скриншот: {screenshot_name}

mean_sum: {mean_sum}
requested_mean_sum: {requested_mean_sum}

diff_extrema: {diff}

Ожидаемый скриншот:
https://files-n.internal.myteam.mail.ru/get/{original_image_file_id}
Скриншот из автотеста:
https://files-n.internal.myteam.mail.ru/get/{image_from_request_file_id}
Разница:
https://files-n.internal.myteam.mail.ru/get/{diff_image_file_id}"""

        response = client.get(
            url=f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendText',
            params={
                'token': os.getenv('BOT_TOKEN'),
                'chatId': os.getenv('DECIDE_CHAT'),
                'text': text,
                'inlineKeyboardMarkup': json.dumps([[
                    {
                        "text": "Заменить скриншот",
                        "callbackData": f"replace|{screenshot_name}",
                        "style": "primary"
                    },
                    {
                        "text": "Оставить старый",
                        "callbackData": f"leave|{screenshot_name}",
                        "style": "primary"
                    }
                ]])
            }
        )
        logger.info(response.url)
        logger.info(response.text)

        return True


@celery_app.task(name="send_report_on_image_diff")
def send_report_on_image_diff_task(
        node_name: str,
        BRANCH_NAME: str,
        test_case: str,
        screenshot_name: str,
        mean_sum: float,
        requested_mean_sum: float,
        diff: float,
        original_image: Image,
        image_from_request: Image,
        diff_image: Image,
):
    return send_report_on_image_diff(
        node_name,
        BRANCH_NAME,
        test_case,
        screenshot_name,
        mean_sum,
        requested_mean_sum,
        diff,
        original_image, image_from_request, diff_image
    )


@logger.catch(default=True)
def send_report_on_new_image(
        node_name: str,
        BRANCH_NAME: str,
        test_case: str,
        origin_image_path: str
):
    logger.info('Started send_report_on_new_image')
    logger.info(origin_image_path)

    with open(origin_image_path, 'rb') as f:
        screenshot_bytes_io = io.BytesIO(f.read())

    caption = f"""Node Name: {node_name}
Branch: {BRANCH_NAME}

Тест-кейс: {test_case}
Название скриншота: {origin_image_path}

Так как в папке Origin не найден файл с таким названием - создан новый"""

    with Session() as client:
        response = client.post(
            url=f'{os.getenv("BOT_API_URL")}/bot/v1/messages/sendFile',
            params={
                'token': os.getenv('BOT_TOKEN'),
                'chatId': os.getenv('DECIDE_CHAT'),
                'caption': caption
            },
            files={"file": screenshot_bytes_io}
        ).json()
        logger.info(response)

        return True


@celery_app.task(name="send_report_on_new_image")
def send_report_on_new_image_task(
        node_name: str,
        BRANCH_NAME: str,
        test_case: str,
        origin_image_path: str
):
    return send_report_on_new_image(
        node_name, BRANCH_NAME, test_case, origin_image_path
    )
