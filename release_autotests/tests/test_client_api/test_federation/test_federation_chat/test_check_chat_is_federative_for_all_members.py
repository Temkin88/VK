import allure
import pytest
from pyvkteamsclient.client import DesktopClient
from support.markers import SANDBOX
from tests.test_client_api.test_federation.common import (
    find_chat_by_some_criterion,
    find_events_with_is_federation_true,
    check_event_with_federation_list,
)


@allure.id("1535449")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Группы")
@allure.feature("Признак федеративности чата")
@allure.title("Наличие признака федеративности у группового чата для всех его участников")
@SANDBOX
@pytest.mark.parametrize(
    "chat_fixture_prefix",
    [
        "channel",
        "group",
    ],
)
@pytest.mark.parametrize(
    ("chat_fixture_name_suffix", "isFederation"),
    [
        ("GA2", True),
        ("GA1", False),
    ],
)
def test_check_chat_is_federative_for_all_members(
    request, chat_fixture_name_suffix, chat_fixture_prefix, isFederation, fetch_until_empty_answer_with_filter
):
    with allure.step("Создаем тестовый чат"):
        chat_name, _, _ = request.getfixturevalue(chat_fixture_prefix + "_" + chat_fixture_name_suffix)
    with allure.step("Получаем участников этого чата"):
        fixtures = request.fixturenames
        for fixture_name in fixtures:
            fixture_value = request.getfixturevalue(fixture_name)
            if isinstance(fixture_value, DesktopClient):
                chat_member = fixture_value
                with allure.step("Проверяем валидное значение признака федеративности событий"):
                    events = fetch_until_empty_answer_with_filter(chat_member)
                    event_types_with_is_federation_true_value = find_events_with_is_federation_true(events)
                    assert (
                        check_event_with_federation_list(event_types_with_is_federation_true_value) == isFederation
                    ), "Неверный перечень событий"
                with allure.step(
                    f"Проверяем валидное значение признака федеративности у чата пользователем {chat_member.uin}"
                    f" в rapi/search"
                ):
                    sn = find_chat_by_some_criterion(chat_member, chat_name, {"isFederation": isFederation})
                    assert sn, "Неверное значение признака федеративности"

                with allure.step(
                    f"Проверяем валидное значение признака федеративности у чата пользователем {chat_member.uin}"
                    f" в rapi/getChatInfo"
                ):
                    response = chat_member.rapi_getChatInfo(sn=sn)
                    assert response["status"]["code"] == 20000, "Неверный статус ответа"
                    if "federation" in response["results"]:
                        assert response["results"]["isFederation"] == isFederation, (
                            "Неверный признак федеративности чата"
                        )
                    elif not isFederation:
                        assert True, "Неверный признак федеративности чата"
