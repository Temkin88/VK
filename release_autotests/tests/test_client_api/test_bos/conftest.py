import logging

import allure
import pytest

from pyvkteamsclient.client import DesktopClient

log = logging.getLogger(__name__)


@allure.title("Подготовка треда для тестов")
@pytest.fixture(scope="session", params=["group", "channel"])
def prepared_thread(request, auth_account, opponent_account, prepare_test_chats, ENV_PLATFORM):
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    _, _, group, channel = prepare_test_chats

    target = group if request.param == "group" else channel

    msg_id = auth_account.send_basic_message(
        sn=target,
        text="Message for threads test",
    )

    thread_id = auth_account.add_thread(chat_id=target, msg_id=msg_id)

    opponent_account.rapi_thread_subscribe(
        threadId=thread_id,
    )

    opponent_account.rapi_eventSubscribe(
        subscriptions=[
            {
                "type": "threadUpdate",
                "data": {
                    "threads": [thread_id],
                },
            }
        ],
    )

    return target, msg_id, thread_id


@pytest.fixture(scope="module")
def account_with_event_stream(
    ENV_PLATFORM,
    accounts_data,
    main_api,
    binary_api,
    api_version,
    session,
    forced_ip,
    imap_serv,
):
    account = accounts_data[0]

    main_account = DesktopClient(
        uin=account.get("uin") or account.get("username"),
        session=session,
        api_url=main_api,
        binary_api_url=binary_api,
        api_ver=api_version,
        forced_ip=forced_ip,
        env=ENV_PLATFORM,
        email_password=account["password"],
        email_url=imap_serv,
        assert_caps=[
            "094613504c7f11d18222444553540000",
            "094613514c7f11d18222444553540000,094613503c7f11d18222444553540000",
            "094613534c7f11d18222444553540000,094613544c7f11d18222444553540000",
            "094613594c7f11d18222444553540000,0946135b4c7f11d18222444553540000",
            "0946135a4c7f11d18222444553540000,0946135c4c7f11d18222444553540000",
            "0946135e4c7f11d18222444553540000,1f99494e76cbc880215d6aeab8e42268",
            "0946135d4c7f11d18222444553540000,a20c362cd4944b6ea3d1e77642201fd8",
            "7d552c211af3414b932db31a65e01b0a",
        ],
    )

    main_account.restore_privacy_settings()

    try:
        main_account.send_basic_message(
            sn=main_account.uin,
            text="test messages",
        )
        main_account.fetch(timeout=300)

        for chat_id in [
            chat_list["eventData"]["aimId"] for chat_list in main_account.events if chat_list["type"] == "myInfo"
        ]:
            main_account.wim_buddyList_hideChat(buddy=chat_id)
            main_account.wim_buddyList_removeBuddy(buddy=chat_id)
    except Exception as error:
        main_account.logger.error(error)

    yield main_account

    main_account.wim_aim_endSession()
