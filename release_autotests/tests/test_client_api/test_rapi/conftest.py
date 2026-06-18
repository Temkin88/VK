import concurrent.futures
import logging

import allure
import pytest

log = logging.getLogger(__name__)


@allure.title("Очистка чатов после тестов")
@pytest.fixture(scope="session", autouse=True)
def clean_chats(auth_account, opponent_account, logger, ENV_PLATFORM):
    yield

    def mod_chat(Account, chat_id):
        Account.mod_chat(
            sn=chat_id,
            public=False,
            joinModeration=True,
        )

        chat_info = Account.rapi_getChatInfo(sn=chat_id)["results"]

        chat_members = list(
            filter(
                lambda x: x["sn"] != Account.uin,
                chat_info["members"],
            ),
        )

        if chatId.endswith("chat.agent") and chat_members:
            Account.rapi_blockChatMember(
                sn=chat_id,
                members=[member["sn"] for member in chat_members],
            )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for account in (auth_account, opponent_account):
            for chatId in account.created_chats:
                futures.append(
                    executor.submit(
                        mod_chat,
                        account,
                        chatId,
                    ),
                )

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as error:
                log.error(error)
