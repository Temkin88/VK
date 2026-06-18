import logging
import time
from pathlib import Path

import allure
from playwright.sync_api import Page, expect

from pyvkteamsclient.client import DesktopClient

logger = logging.getLogger(__name__)


@allure.step("Авторизуемся в аккаунт {account}")
def authorize(page: Page, account: DesktopClient) -> Page:
    with allure.step('Ищем кнопку "Принять и продолжить"'):
        gdpr_button = page.locator(".imButton")

    with allure.step("Проверяем что она видна"):
        expect(gdpr_button).to_be_visible()

    if account.env in ["TARM", "PRE_TARM"]:
        with allure.step("Проставляем чек-боксы соглашений"):
            for checkbox in page.query_selector_all(".im-tickbox"):
                checkbox.click()

    with allure.step("Проверяем что она кликабельна"):
        gdpr_button.click()

    with allure.step("Вводим логин"):
        page.locator(
            ".imAuthPhone" if account.env == "ICQ" else ".imAuthLogin",
        ).fill(
            account.phone if account.env == "ICQ" else account.uin,
        )

        page.locator(".imButton").click()

    otp_token = account.get_otp_token()

    with allure.step("Вводим OTP-код"):
        page.locator(
            ".imAuthCode" if account.env == "ICQ" else ".imAuthPassword",
        ).fill(otp_token)

        if account.env != "ICQ":
            page.locator(".imButton").click()

    return page


@allure.step("Открываем чат с аккаунтом {chat_id} через поиск")
def open_chat(page: Page, chat_id: str) -> Page:
    with allure.step(f"Вводим в поиск {chat_id}"):
        page.locator('//input[@class="im-search-field"]').first.fill(chat_id)

    with allure.step("Находим в результатах поиска"):
        time.sleep(5)

        for element in page.query_selector_all(".imSearchEntry"):
            if element.get_attribute("data-sn") == chat_id:
                search_result = element
                break
        else:
            raise ValueError(f".imSearchEntry[data-sn={chat_id}] not found")

    with allure.step("Кликаем по профилю в результатах поиска"):
        search_result.click()

    with allure.step("Проверяем что открылся чат"):
        page.locator("im-chat__history-wrap")

    return page


@allure.step("Отправляем сообщение в чат {chat_id}")
def send_message(page: Page, chat_id: str) -> Page:
    open_chat(page, chat_id)

    with allure.step("Заполняем инпут текста"):
        page.locator(".im-chat__input-field").fill("Test text")

    with allure.step("Нажимаем на отправку сообщения"):
        page.locator(".im-chat__input-action__send").click()

    with allure.step("Проверяем что сообщение отправилось"):
        expect(page.locator(".imTextBlock", has_text="Test text").first).to_be_visible()

    return page


@allure.step("Отправялем фото в чат {chat_id}")
def send_file(page: Page, chat_id: str, path: Path) -> Page:
    open_chat(page, chat_id)

    with allure.step("Открываем контекстное меню слева"):
        page.locator(".im-chat__input-sub-action").click()

    time.sleep(5)

    with allure.step("Выбираем фото"):
        page.locator(".im-attachmenu__item").locator('//input[@type="file"]').first.set_input_files(path)

    with allure.step("Проверяем что появилось модальное окно отправки файла"):
        expect(page.locator(".im-filebox")).to_be_visible()

    with allure.step("Подтверждаем отправку"):
        page.locator(".im-filebox").locator(".imButton").last.click()

    with allure.step("Проверяем что отобразилось окно отправки файла"):
        page.locator(".im-file-wrapper")

    return page
