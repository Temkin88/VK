import allure

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("79652")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Чаты")
@allure.feature("Список заблокированных участников чата")
@allure.title("Просмотр списка заблокированных участников чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_get_blacklist_contacts(
    prepare_test_chats,
    add_invite_blacklist,
):
    main_acc, opponent, _, _ = prepare_test_chats

    uins_list = [
        "1000000001",
        "1000000002",
        opponent.uin,
    ]

    with allure.step("Добавляем uin в черный список"):
        add_invite_blacklist(account=main_acc, users_list=uins_list)

    with allure.step("Проверяем что сотрудник появился в списке заблокированных участников"):
        response = main_acc.rapi_privacy_groups_inviteBlacklist_getBlacklistedContacts()

        assert response["status"]["code"] == 20000, "Failed request"
        assert uins_list[2] in response["results"]["blacklist"], "Uin not in blacklist"
        assert all(uin not in response["results"]["blacklist"] for uin in uins_list[:2]), "Uin in blacklist"
