import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, SLA, PRE_SAAS


@allure.id("66415")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений")
@allure.title("Измение состояние диалога")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
# @pytest.mark.parametrize('exclude_dlg', ['call', 'mention', 'pttListen'])
@pytest.mark.parametrize("stranger_dlg", [True, False])
def test_rapi_set_dlg_state(
    prepare_test_chats,
    # exclude_dlg,
    stranger_dlg,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем добавление, наличие и удаление реакции к сообщению
    """

    main_acc, opponent, group, channel = prepare_test_chats

    chat = group

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = main_acc.send_basic_message(
            sn=chat,
            text="Test msg for reactions",
        )

    sender_old_chat_history = main_acc.rapi_getHistory(
        sn=chat,
    )
    receiver_old_chat_history = opponent.rapi_getHistory(
        sn=chat,
    )

    with allure.step("Пытаемся изменить состояние диалога"):
        event_filter.start_point()

        (
            opponent.rapi_setDlgState(
                sn=chat,
                stranger=stranger_dlg,
                exclude=[],
                lastRead=msg_id,
            ),
            "Failed to change dlg state",
        )

        main_acc.wim_im_setTyping(
            t=chat,
        )

    with allure.step("Проверяем что ID последнего прочитанного обновилось у прочитавшего"):
        receiver_updated_chat_history = opponent.rapi_getHistory(
            sn=chat,
        )

        receiver_old_lastRead = receiver_old_chat_history["results"]["yours"].get("lastRead", -1)
        receiver_updated_lastRead = receiver_updated_chat_history["results"]["yours"]["lastRead"]

        assert receiver_old_lastRead != receiver_updated_lastRead, "Wrong lastRead msg ID in msg receiver chat history"
        assert msg_id == int(receiver_updated_chat_history["results"]["yours"]["lastRead"]), (
            "Wrong lastRead msg ID in msg receiver chat history"
        )

    with allure.step("Проверяем что у отправителя в getHistory у сообщения обновился readCount"):
        sender_updated_chat_history = main_acc.rapi_getHistory(sn=chat)

        old_message_info = list(
            filter(
                lambda x: int(x["msgId"]) == msg_id,
                sender_old_chat_history["results"]["messages"],
            ),
        )[-1]
        updated_message_info = list(
            filter(
                lambda x: int(x["msgId"]) == msg_id,
                sender_updated_chat_history["results"]["messages"],
            ),
        )[-1]

        assert old_message_info.get("readsCount", 0) != updated_message_info["readsCount"], (
            "Wrong readsCount for messaage"
        )

    with allure.step("Проверяем что пришло событие histDlgState"):
        fetch_until_empty_answer(main_acc)

        histDlgState_event_found = False

        for event in event_filter(main_acc.events, "histDlgState"):
            event_data = event["eventData"]

            if event_data["sn"] == chat and event_data["lastMsgId"] == msg_id:
                histDlgState_event_found = True

        assert histDlgState_event_found, "Event histDlgState not found"

    with allure.step("Проверяем что пришло событие chatHeadsUpdate"):
        chatHeadsUpdate_event_found = False

        for event in event_filter(main_acc.events, "chatHeadsUpdate"):
            event_data = event["eventData"]

            if event_data["sn"] == chat:
                for postion in event_data["positions"]:
                    if postion["msgId"] == msg_id and opponent.uin in str(postion["heads"]):
                        chatHeadsUpdate_event_found = True

        assert chatHeadsUpdate_event_found, "Event chatHeadsUpdate not found"
