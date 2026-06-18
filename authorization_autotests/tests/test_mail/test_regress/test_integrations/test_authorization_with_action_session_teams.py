# import allure
#
# from api.client.adapter import ClientAdapterWs, ClientAdapterTeamsOTP
# from api.client.client import UserClientWS, UserClientTeamsOTP
# from api.ws.ws import WSUser
# from markers import WS
#
#
# @allure.id("2489856")
# @allure.label("layer", "api_layer")
# @allure.severity(allure.severity_level.NORMAL)
# @allure.story("Админка")
# @allure.feature("Интеграционное тестирование VKT+WorkSpace")
# @allure.title("Авторизация при наличии активной сессии в мессенджере")
# @WS
# def test_authorization_with_action_session_teams(get_config):
#     url = "https://auth-test.vkteams.vkwm.ru"
#     login_ws = "1@otp.auth-test.vkteams.vkwm.ru"
#     pass_ws = "Q-12345"
#
#     api_url = get_config(f"u.{url.replace("https://", "vkt-", 1)}")['api-urls']['main-api']
#     api_ver = get_config(f"u.{url.replace("https://", "vkt-", 1)}")['api-version']
#     imap_url = url.replace("https://", "imap.", 1)
#
#     user_teams = UserClientTeamsOTP(
#         api_url=api_url,
#         api_ver=api_ver,
#         uin=login_ws,
#         password=pass_ws,
#         imap_url=imap_url,
#         login_adapter=ClientAdapterTeamsOTP(base_url=api_url),
#     )
#     user = user_teams.login(fix_otp=False)
#
#     search_chat = user_teams.rapi_search(url=api_url, api_version=api_ver,keyword="mailbot", aimsid=user[0], withoutBlocked=False, withoutBots=False).json()
#     sn_chat = search_chat['results']['data'][0]['sn']
#     teams_get_history = user_teams.rapi_getHistory(url=api_url, sn=sn_chat, api_version=api_ver, aimsid=user[0]).json()
#     teams_message_id = teams_get_history['results']['messages'][0]['inlineKeyboardMarkup'][0][0]['url'].split("message/")[1]
#
#     assert "1@otp.auth-test.vkteams.vkwm.ru" in user[0]
#     assert "https://u.vkt-auth-test.vkteams.vkwm.ru" in user[1]
#
#     user_ws = UserClientWS(
#         base_url=url,
#         username=login_ws,
#         password=pass_ws,
#         login_adapter=ClientAdapterWs(base_url=url),
#     )
#
#     user_ws.login()
#     user_check = user_ws.auth_check()
#     assert "1@otp.auth-test.vkteams.vkwm.ru" == user_check["data"]["email"]
#     assert "1@otp.auth-test.vkteams.vkwm.ru" in user_check["data"]["list"]