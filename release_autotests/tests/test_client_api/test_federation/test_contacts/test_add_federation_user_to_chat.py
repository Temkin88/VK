import allure
import lorem
import pytest
from support.markers import SANDBOX
from tests.test_client_api.test_federation.common import generate_uniq_chat_name


@allure.id("1212709")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Добавление федеративного пользователя в групповой чат")
@allure.title("Добавление федеративного пользователя в групповой чат")
@SANDBOX
@pytest.mark.parametrize("defaultRole", ["member", "readonly"])
@pytest.mark.parametrize(
    ("local_fed_account1_var", "remote_fed_account1_var", "local_fed_account2_var"),
    [
        ("fed_acc_on_host1_host2", "fed_acc_on_host2_host1", "fed_acc2_on_host1_host2"),
        ("fed_acc_on_host2_host1", "fed_acc_on_host1_host2", "fed_acc2_on_host2_host1"),
    ],
)
def test_add_federation_user_to_chat(
    request,
    local_fed_account1_var,
    remote_fed_account1_var,
    local_fed_account2_var,
    get_chat_sn_from_event,
    defaultRole,
    check_message_in_history,
):
    local_fed_acc1 = request.getfixturevalue(local_fed_account1_var)
    remote_fed_acc1 = request.getfixturevalue(remote_fed_account1_var)
    local_fed_acc2 = request.getfixturevalue(local_fed_account2_var)

    msg_text_list = [lorem.sentence(), lorem.sentence(), lorem.sentence()]
    acc_list = [local_fed_acc1, remote_fed_acc1, local_fed_acc2]
    chat_for_cheks_dict = {}
    with allure.step(
        f"Пользователь из инсталяции {acc_list[0].api_url.replace('https://u', '')}"
        "создает чат с федеративнми пользователями"
    ):
        chat_name = generate_uniq_chat_name("Test_chat")
        response = acc_list[0].rapi_createChat(
            name=chat_name, joinModeration=False, defaultRole=defaultRole, members=[acc_list[0].uin]
        )
        chat_id = response["results"]["sn"]

    chat_for_cheks_dict[acc_list[0].api_url.replace("https://u", "")] = chat_id
    with allure.step(
        f"Пользователь из инсталяции {acc_list[0].api_url.replace('https://u', '')} пишет сообщение в чат"
    ):
        send_msg_id = acc_list[0].send_basic_message_by_message_send(
            target=chat_id,
            plain=msg_text_list[0],
        )
        assert send_msg_id is not None, "Не удалось отправить сообщение"

    for i in [1, 2]:
        with allure.step(
            f"Добавляем в чат федеративного пользователя из инсталляции {acc_list[i].api_url.replace('https://u', '')}"
        ):
            response = local_fed_acc1.rapi_group_members_add(sn=chat_id, members=[acc_list[i].uin])
        assert response["status"]["code"] == 20000, f"Не удалось добавить в чат пользователя {acc_list[i].uin}"

        with allure.step(
            f"Пользователь из инсталяции {acc_list[0].api_url.replace('https://u', '')} пишет сообщение в чат"
        ):
            send_msg_id = local_fed_acc1.send_basic_message_by_message_send(
                target=chat_id,
                plain=msg_text_list[i],
            )
            assert send_msg_id is not None, "Не удалось отправить сообщение"

        if acc_list[i].api_url.replace("https://u", "") not in chat_for_cheks_dict:
            with allure.step(
                f"Пользователь из инсталяции {remote_fed_acc1.api_url.replace('https://u', '')} "
                f"получает sn федеративного чата в своей инсталяции"
            ):
                remote_sn = get_chat_sn_from_event(acc_list[i], chat_name)
                assert remote_sn is not None, "Sn чата на инсталяции не доступен"
                chat_for_cheks_dict[acc_list[i].api_url.replace("https://u", "")] = remote_sn

    for i in range(len(acc_list)):
        with allure.step(
            f"Проверяем что {i + 1} пользователю недоступны/доступны сообщения до/после добавления его в чат"
        ):
            for j in range(i, len(msg_text_list)):
                assert (j >= i) == check_message_in_history(
                    acc_list[i],
                    sn=chat_for_cheks_dict[acc_list[i].api_url.replace("https://u", "")],
                    msg_text=msg_text_list[j],
                ), "Ошибка доступа к сообщению"
