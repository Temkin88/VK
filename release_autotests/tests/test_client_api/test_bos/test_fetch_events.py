import time

import allure
import pytest
from jsondiff import diff

from support.cases.drafts import draft_parts
from support.cases.formatted_msgs import formatted_msgs
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, SLA, PRE_SAAS
from support.modules.dantic import BuddyListEventModel, MyInfoModel


@allure.id("26952")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("События на старте")
@allure.title("Получение события buddylist")
def test_buddy_list_event_on_start(
    fetch_events_till_empty_queue,
    logger,
):
    for account in fetch_events_till_empty_queue:
        with allure.step(f"Проверяем наличие события buddylist у {account}"):
            for event in filter(lambda x: x["type"] == "buddylist", account.events):
                BuddyListEventModel.parse_obj(event)


@allure.id("26953")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("События на старте")
@allure.title("Получение события myInfo")
def test_my_info_event_on_start(
    fetch_events_till_empty_queue,
    logger,
):
    for account in fetch_events_till_empty_queue:
        with allure.step(f"Проверяем наличие события myInfo у {account}"):
            for event in filter(lambda x: x["type"] == "myInfo", account.events):
                MyInfoModel.parse_obj(event)


@pytest.fixture
def build_basic_msg_text(
    photo,
    voice,
    sticker,
):
    def build(message: dict[str, str]) -> str:
        if message["type"] == "text":
            return message["body"]
        elif message["type"] == "photo":
            return photo
        elif message["type"] == "voice":
            return voice
        elif message["type"] == "sticker":
            return sticker
        else:
            raise ValueError

    return build


@allure.title("Подготовка тестовых чатов")
@pytest.fixture(scope="session")
def prepare_test_chats_for_fetch_events(
    request,
    opponent_account,
    auth_account,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account],
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account],
        )

    return auth_account, opponent_account, group, channel


@pytest.fixture
def switch_targets(
    auth_account,
    opponent_account,
    prepare_test_chats_for_fetch_events,
):
    _, _, group_chat, channel_chat = prepare_test_chats_for_fetch_events

    def switch(target_chat: str):
        if target_chat == "favorite":
            target_chat = auth_account.uin
            fetch_chat = auth_account.uin
            sender = auth_account
        elif target_chat == "private":
            target_chat = auth_account.uin
            fetch_chat = opponent_account.uin
            sender = opponent_account
        elif target_chat == "group":
            target_chat = group_chat
            fetch_chat = group_chat
            sender = opponent_account
        elif target_chat == "channel":
            target_chat = channel_chat
            fetch_chat = channel_chat
            sender = opponent_account
        else:
            raise ValueError

        return target_chat, fetch_chat, sender

    return switch


@allure.id("26956")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "target_chat",
    [
        "favorite",
        "private",
        "group",
        # 'channel'
    ],
    ids=lambda x: f"chat:{x}",
)
@pytest.mark.parametrize(
    "message",
    [
        {"type": "text", "body": "Text message for fetch events test"},
        {"type": "photo"},
        {"type": "voice"},
        {"type": "sticker"},
    ],
    ids=lambda x: "msg:{type}".format(**x),
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о входящем сообщении")
def test_incoming_basic_message_in_chat_event(
    fetch_events_till_empty_queue,
    auth_account,
    opponent_account,
    logger,
    event_filter,
    target_chat,
    message,
    build_basic_msg_text,
    switch_targets,
    fetch_until_empty_answer_with_filter,
):
    text = build_basic_msg_text(message)

    target_chat, fetch_chat, sender = switch_targets(target_chat)

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = sender.send_basic_message(target_chat, text)

    with allure.step("Ищем событие о сообщении"):
        event_found_and_checked = False

        for _ in range(3):
            with allure.step(f"Попытка #{_}"):
                for event in fetch_until_empty_answer_with_filter(auth_account, "histDlgState"):
                    if event["eventData"]["sn"] == fetch_chat and event["eventData"]["lastMsgId"] == msg_id:
                        event_found_and_checked = text in [x["text"] for x in event["eventData"]["tail"]["messages"]]
                    if event_found_and_checked:
                        break
            if event_found_and_checked:
                break
            time.sleep(1)

    assert event_found_and_checked, f"{sender.env}:histDlgState_event_not_found"


@allure.id("26957")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о смене статуса")
@pytest.mark.parametrize(
    ("status_type", "media", "text", "duration"),
    [
        ("predefined", "\U0001f44d", "test", 32400),
        ("predefined", "🥐", "test 🍔", 32400),
        ("predefined", "🥐", None, 32460),
        ("empty", None, "test 🍔", None),
        ("predefined", "🥐", None, None),
        ("empty", None, None, None),
    ],
)
def test_status_set_event(
    fetch_events_till_empty_queue,
    logger,
    auth_account,
    opponent_account,
    event_filter,
    duration,
    media,
    status_type,
    text,
    fetch_until_empty_answer_with_filter,
):
    with allure.step(f"Подписываемся на userState пользователя {opponent_account}"):
        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "status",
                    "data": {
                        "contacts": [opponent_account.uin],
                    },
                }
            ],
        )

    with allure.step(f"Меняем статус у пользователя {opponent_account}"):
        assert (
            opponent_account.rapi_status_set(
                _type=status_type,
                media=media,
                text=text,
                duration=duration,
            )["status"]["code"]
            == 20000
        )

    with allure.step("Ищем событие об смене статуса"):
        event_found_and_checked = False

        for _ in range(3):
            with allure.step(f"Попытка #{_}"):
                for event in fetch_until_empty_answer_with_filter(auth_account, "status"):
                    data = event["eventData"]
                    try:
                        assert data["sn"] == opponent_account.uin, "User not equal"
                        assert data.get("media") == media, "Media not equal"
                        assert data["type"] == status_type, "Type not equal"
                        event_found_and_checked = True
                    except AssertionError as error:
                        logger.error(error)

                    if event_found_and_checked:
                        break

            if event_found_and_checked:
                break
            else:
                time.sleep(1)

        assert event_found_and_checked, "Status event not found"


@allure.id("26958")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "target_chat",
    [
        "favorite",
        "private",
        "group",
        "channel",
    ],
    ids=lambda x: f"chat:{x}",
)
@pytest.mark.parametrize(
    "draft",
    draft_parts,
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о черновике при включенном функционале")
def test_draft_enabled_in_chat_event(
    fetch_events_till_empty_queue,
    auth_account,
    opponent_account,
    logger,
    event_filter,
    target_chat,
    draft,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
    is_draft_enabled,
):
    if not is_draft_enabled:
        pytest.skip("Drafts are disabled in myteam-config")

    _, _, group_chat, channel_chat = prepare_test_chats

    if target_chat == "favorite" or target_chat == "private":
        target_chat = auth_account.uin
    elif target_chat == "group":
        target_chat = group_chat
    elif target_chat == "channel":
        target_chat = channel_chat
    else:
        raise ValueError

    with allure.step(f"Сохраняем черновик в чате {target_chat}"):
        assert (
            auth_account.rapi_draft_set(
                sn=target_chat,
                parts=draft,
            )["status"]["code"]
            == 20000
        )

    with allure.step("Ищем событие черновика"):
        event_found_and_checked = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "draft"):
            try:
                assert event["eventData"]["sn"] == target_chat, "Not matched"
                assert event["eventData"]["parts"] == draft, "Not matched"

                event_found_and_checked = True
            except AssertionError as error:
                logger.error(error)

            if event_found_and_checked:
                break

        assert event_found_and_checked, "Draft (full) event not found"

    with allure.step(f"Сохраняем черновик в чате {target_chat}"):
        assert (
            auth_account.rapi_draft_set(
                sn=target_chat,
                parts=[],
            )["status"]["code"]
            == 20000
        )

    with allure.step("Ищем событие черновика"):
        event_found_and_checked = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "draft"):
            try:
                assert event["eventData"]["sn"] == target_chat, "Not matched"
                assert event["eventData"]["parts"] == [], "Not matched"

                event_found_and_checked = True
            except AssertionError as error:
                logger.error(error)

            if event_found_and_checked:
                break

        assert event_found_and_checked, "Draft (empty) event not found"


@allure.id("26959")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "user_role",
    [
        "member",
        "readonly",
    ],
    ids=[
        "group",
        "channel",
    ],
)
@pytest.mark.parametrize(
    "receiver",
    [
        "creator",
        "member",
    ],
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("События")
@allure.feature("Чаты")
@allure.title("Получение событий после создания чата")
def test_events_on_chat_creation(
    auth_account,
    opponent_account,
    event_filter,
    user_role,
    receiver,
    fetch_until_empty_answer_with_filter,
    fetch_events_till_empty_queue,
):
    """
    Проверяем полученные события ('histDlgState', 'diff') после создания чата
    :param auth_account: Основной аккаунт
    :param opponent_account: Дополнительный аккаунт
    :param event_filter: Фикстура для фильтрации событий по типу
    :param user_role: Параметризация для роли создания чата
    :param receiver: Параметризация для определения роли аккаутна
    :param fetch_until_empty_answer: Фикстура предназначенная для выборки событий до пустого значения
    :param fetch_events_till_empty_queue: Фикстура предназначенная для выборки событий до тех пор, пока очередь не
    опустеет
    """
    event_filter.start_point()

    with allure.step("Создаем группу"):
        chat_name = "Test group for fetchEvent"

        chat_id = auth_account.create_chat(
            name=chat_name,
            members=[
                opponent_account,
            ],
            defaultRole=user_role,
        )

    with allure.step("Ищем события о создании чата"):
        receiver = auth_account if receiver == "creator" else opponent_account

        histDlgState_event_found_and_checked = False
        diff_event_found_and_checked = False

        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(receiver, "histDlgState", "diff"):
                if event["type"] == "histDlgState":
                    try:
                        assert event["eventData"]["sn"] == chat_id, "Another chat event"
                        assert {
                            auth_account.uin,
                            opponent_account.uin,
                            chat_id,
                        } == {x["sn"] for x in event["eventData"].get("persons", [])}, "Another chat event"
                        histDlgState_event_found_and_checked = True
                    except AssertionError:
                        pass
                else:
                    diff_event_found_and_checked = True

                if histDlgState_event_found_and_checked and diff_event_found_and_checked:
                    break

            if histDlgState_event_found_and_checked and diff_event_found_and_checked:
                break
            else:
                time.sleep(1)

        assert histDlgState_event_found_and_checked, "histDlgState not found"
        assert diff_event_found_and_checked, "diff not found"


@allure.id("26960")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "target_chat",
    [
        "favorite",
        "private",
        "group",
        "channel",
    ],
    ids=lambda x: f"chat:{x}",
)
@pytest.mark.parametrize(
    "draft",
    draft_parts,
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о черновике при выключенном функционале")
def test_draft_disabled_in_chat_event(
    fetch_events_till_empty_queue,
    auth_account,
    opponent_account,
    logger,
    event_filter,
    target_chat,
    draft,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
    is_draft_enabled,
):
    if is_draft_enabled:
        pytest.skip("Drafts are enabled in myteam-config")

    _, _, group_chat, channel_chat = prepare_test_chats

    if target_chat == "favorite" or target_chat == "private":
        target_chat = auth_account.uin
    elif target_chat == "group":
        target_chat = group_chat
    elif target_chat == "channel":
        target_chat = channel_chat
    else:
        raise ValueError

    with allure.step(f"Сохраняем черновик в чате {target_chat}"):
        assert (
            auth_account.rapi_draft_set(
                sn=target_chat,
                parts=draft,
            )["status"]["code"]
            == 20000
        )

    with allure.step("Ищем событие черновика"):
        event_found_and_checked = False

        for _ in fetch_until_empty_answer_with_filter(auth_account, "draft"):
            event_found_and_checked = True

        assert not event_found_and_checked, "Draft event found"

    with allure.step(f"Сохраняем черновик в чате {target_chat}"):
        assert (
            auth_account.rapi_draft_set(
                sn=target_chat,
                parts=[],
            )["status"]["code"]
            == 20000
        )

    with allure.step("Ищем событие черновика"):
        event_found_and_checked = False

        for _ in fetch_until_empty_answer_with_filter(auth_account, "draft"):
            event_found_and_checked = True

        assert not event_found_and_checked, "Draft event found"


@allure.id("27262")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "target_chat",
    [
        "group",
        "channel",
    ],
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("События")
@allure.feature("Треды")
@allure.title("Получение событий после создания треда")
def test_events_on_thread_creation(
    auth_account,
    opponent_account,
    prepare_test_chats,
    target_chat,
    event_filter,
    fetch_until_empty_answer_with_filter,
    ENV_PLATFORM,
):
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    _, _, group_chat, channel_chat = prepare_test_chats

    if target_chat == "group":
        target_chat = group_chat
    elif target_chat == "channel":
        target_chat = channel_chat
    else:
        raise ValueError

    with allure.step("Отправляем сообщение в чат"):
        msg_id = auth_account.send_basic_message(
            sn=target_chat,
            text="Msg for threads events test",
        )

    with allure.step("Создаем от него тред"):
        thread_id = opponent_account.add_thread(
            chat_id=target_chat,
            msg_id=msg_id,
        )

    with allure.step("Проверяем события после создания"):
        unreadThreadsCount_found = False
        threadUpdate_found = False

        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(
                opponent_account,
                "unreadThreadsCount",
                "threadUpdate",
            ):
                if event["type"] == "unreadThreadsCount":
                    unreadThreadsCount_found = True
                elif event["type"] == "threadUpdate":
                    data = event["eventData"]
                    if (
                        data["parentTopic"]["chatId"] == target_chat
                        and data["parentTopic"]["messageId"] == msg_id
                        and data["threadId"] == thread_id
                        and data["you"]["subscriber"]
                    ):
                        threadUpdate_found = True

                elif unreadThreadsCount_found and threadUpdate_found:
                    break
            if unreadThreadsCount_found and threadUpdate_found:
                break
            else:
                time.sleep(1)

        assert unreadThreadsCount_found
        assert threadUpdate_found


@allure.id("27258")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "target_chat",
    [
        "favorite",
        "private",
        "group",
        "channel",
    ],
    ids=lambda x: f"chat:{x}",
)
@pytest.mark.parametrize(
    "message",
    formatted_msgs,
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о входящем сообщении")
def test_incoming_formatted_message_in_chat_event(
    fetch_events_till_empty_queue,
    auth_account,
    opponent_account,
    logger,
    event_filter,
    target_chat,
    message,
    build_basic_msg_text,
    switch_targets,
    fetch_until_empty_answer_with_filter,
):
    target_chat, fetch_chat, sender = switch_targets(target_chat)

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = sender.wim_im_sendIM(
            t=target_chat,
            parts=message,
        )["response"]["data"]["histMsgId"]

    with allure.step("Ищем событие о сообщении"):
        event_found_and_checked = False

        for _ in range(3):
            with allure.step(f"Попытка #{_}"):
                for event in fetch_until_empty_answer_with_filter(auth_account, "histDlgState"):
                    data = event["eventData"]
                    if data["sn"] == fetch_chat and data["lastMsgId"] == msg_id:
                        event_found_and_checked = not bool(diff(message, data["tail"]["messages"][0]["parts"]))
                    if event_found_and_checked:
                        break
            if event_found_and_checked:
                break
            else:
                time.sleep(1)

    assert event_found_and_checked, f"{sender.env}:histDlgState_event_not_found"


@allure.id("42356")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "message",
    formatted_msgs,
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о входящем сообщении")
def test_incoming_formatted_message_in_private_chat_event(
    fetch_events_till_empty_queue,
    auth_account,
    opponent_account,
    logger,
    event_filter,
    message,
    build_basic_msg_text,
    fetch_until_empty_answer_with_filter,
):
    with allure.step("Отправляем тестовое сообщение"):
        msg_id = opponent_account.wim_im_sendIM(
            t=auth_account.uin,
            parts=message,
        )["response"]["data"]["histMsgId"]

        logger.info(f"{opponent_account.uin}:{auth_account.uin}:{msg_id}")

    with allure.step("Ищем событие о сообщении"):
        event_found_and_checked = False

        for _ in range(3):
            with allure.step(f"Попытка #{_}"):
                for event in fetch_until_empty_answer_with_filter(auth_account, "histDlgState"):
                    data = event["eventData"]
                    if data["sn"] == opponent_account.uin and data["lastMsgId"] == msg_id:
                        event_found_and_checked = not bool(diff(message, data["tail"]["messages"][0]["parts"]))
                    if event_found_and_checked:
                        break
            if event_found_and_checked:
                break
            else:
                time.sleep(1)

    assert event_found_and_checked, f"{auth_account.env}:histDlgState_event_not_found"


@allure.id("27263")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "message",
    [
        "Message in thread for fetch events",
        *formatted_msgs,
    ],
    ids=type,
)
@pytest.mark.parametrize(
    "receiver",
    [
        "sender",
        "sub",
    ],
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о сообщении в треде")
def test_outcoming_message_in_thread_events(
    auth_account,
    opponent_account,
    prepared_thread,
    event_filter,
    message,
    receiver,
    fetch_until_empty_answer,
):
    target, msg_id, thread_id = prepared_thread

    with allure.step("Отправляем сообщение в тред"):
        if isinstance(message, str):
            auth_account.send_basic_message(
                sn=thread_id,
                text=message,
            )
        else:
            auth_account.wim_im_sendIM(
                t=thread_id,
                parts=message,
            )["response"]["data"]["histMsgId"]

    with allure.step("Ищем события"):
        for retry_count in range(3):
            try:
                fetch_until_empty_answer(
                    auth_account if receiver == "sender" else opponent_account,
                )

                threadUpdate = False
                unreadThreadsCount = False

                for event in event_filter(
                    (auth_account if receiver == "sender" else opponent_account).events,
                    "threadUpdate",
                    "unreadThreadsCount",
                ):
                    if (
                        event["type"] == "threadUpdate"
                        and event["eventData"]["threadId"] == thread_id
                        and event["eventData"]["repliesCount"] != 0
                    ):
                        threadUpdate = True
                    elif event["type"] == "unreadThreadsCount":
                        unreadThreadsCount = True
                    else:
                        continue

                result = threadUpdate and unreadThreadsCount

                assert result, f"send_message_to_thread_events:{thread_id}"

            except AssertionError as error:
                auth_account.logger.warning(error)
                if retry_count > 1:
                    raise error


@allure.id("27265")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "receiver",
    [
        "sender",
        "sub",
    ],
)
@pytest.mark.parametrize(
    "is_silent_delete",
    [
        True,
        False,
    ],
    ids=[
        "silent",
        "loud",
    ],
)
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("События")
@allure.feature("Сообщения")
@allure.title("Получение события о входящем сообщении")
def test_outcoming_message_delete_in_thread_events(
    auth_account,
    opponent_account,
    prepared_thread,
    event_filter,
    receiver,
    is_silent_delete,
    fetch_until_empty_answer,
):
    target, msg_id, thread_id = prepared_thread

    message = "Message in thread for fetch events"

    with allure.step("Отправляем сообщение в тред"):
        msg_id = auth_account.send_basic_message(
            sn=thread_id,
            text=message,
        )

        fetch_until_empty_answer(
            auth_account if receiver == "sender" else opponent_account,
        )

        event_filter.start_point()

    with allure.step("Удаляем сообщение"):
        auth_account.rapi_delMsgBatch(
            sn=thread_id,
            msgIds=[msg_id],
            silent=is_silent_delete,
        )

    with allure.step("Ищем события"):
        threadUpdate = False
        unreadThreadsCount = False

        for _ in range(3):
            fetch_until_empty_answer(
                auth_account if receiver == "sender" else opponent_account,
            )

            for event in event_filter(
                (auth_account if receiver == "sender" else opponent_account).events,
                "threadUpdate",
                "unreadThreadsCount",
            ):
                if event["type"] == "unreadThreadsCount":
                    unreadThreadsCount = True
                elif event["type"] == "threadUpdate" and event["eventData"]["threadId"] == thread_id:
                    threadUpdate = True

            result = threadUpdate and unreadThreadsCount

            if result:
                break

        assert result, f"delete_message_in_thread_events:{thread_id}"


@allure.id("30198")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("События")
@allure.suite("Галерея чата")
@allure.feature("Просмотр галереи чата")
@allure.title("Получение события galleryNotify")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "chat_type",
    [
        "favorite",
        "private",
        "group",
        "channel",
    ],
)
def test_gallery_changes_event(
    prepare_test_chats,
    chat_type,
    limited_uploaded_common_file_url,
    ENV_PLATFORM,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    auth_account, opponent_account, group, channel = prepare_test_chats

    if chat_type == "favorite":
        chat_id = auth_account.uin
    elif chat_type == "private":
        chat_id = opponent_account.uin
    elif chat_type == "group":
        chat_id = group
    elif chat_type == "channel":
        chat_id = channel
    else:
        raise ValueError(f"Unknown chat_type value: {chat_type}")

    with allure.step("Отправляем файл в чат"):
        event_filter.start_point()

        msg_id = auth_account.send_basic_message(
            sn=chat_id,
            text=limited_uploaded_common_file_url,
        )

    with allure.step("Ищем событие galleryNotify"):
        for event in fetch_until_empty_answer_with_filter(auth_account, "galleryNotify"):
            data = event["eventData"]
            assert msg_id in [entry["id"]["mid"] for entry in data["tail"]["entries"]], (
                f"{auth_account.env}:galleryNotify event not found"
            )
