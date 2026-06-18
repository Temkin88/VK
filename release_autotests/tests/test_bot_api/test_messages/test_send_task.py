import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@pytest.fixture(scope="session")
def task_id(auth_account):
    with allure.step("Создаем задачу"):
        task_id = auth_account.task_add_by_add(
            title=f"Test task [{auth_account.getReqId()}]",
        )

    return task_id


@allure.id("79354")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отправка сообщения с задачей пользователю")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_bot_send_task(
    start_bot,
    auth_account,
    bot_class,
    chat_type,
    task_id,
    prepare_bot_test_chats,
):
    user, opponent, group, channel = prepare_bot_test_chats

    if chat_type == "private":
        chat = auth_account.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Пробуем отправить тестовое сообщение"):
        response = bot_class.send_task(
            chat_id=chat,
            task_id=task_id,
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")
