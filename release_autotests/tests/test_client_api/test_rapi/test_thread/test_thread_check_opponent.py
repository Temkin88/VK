import uuid

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("893726")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Проверка прочитанности сообщения")
@allure.title("Проверка прочитанности сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_thread_check_opponent(
    chat_type,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
    ENV_PLATFORM,
):
    """
    Проверяем изменение порядка тредов
    """
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = main_acc.send_basic_message(
            sn=chat,
            text=f"Test text-{uuid.uuid4().hex}",
        )

    with allure.step("добавляем тред и подписываемся на него"):
        thread_id = main_acc.add_thread(chat_id=chat, msg_id=msg_id)

    with allure.step("Пишем сообщение в тред"):
        msg_id = opponent.send_basic_message(
            sn=thread_id,
            text=f"Test text-{uuid.uuid4().hex}",
        )
    with allure.step("Пытаемся изменить состояние диалога"):
        (
            opponent.rapi_setDlgState(
                sn=chat,
                stranger=True,
                exclude=[],
                lastRead=msg_id,
            ),
            "Failed to change dlg state",
        )

        main_acc.wim_im_setTyping(
            t=chat,
        )

    with allure.step("Ишем событие chatHeadsUpdate"):
        event_found = False
        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(main_acc, "chatHeadsUpdate"):
                event_data = event["eventData"]
                if chat == event_data["sn"]:
                    event_found = True
                    break
            if event_found:
                break
        assert event_found, "Event chatHeadsUpdate not found"
