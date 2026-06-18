import allure

from support.markers import SANDBOX


@allure.id("79671")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление статусами пользователя")
@allure.title(
    "Получение полного списка всех возможных автостатусов пользователя",
)
@SANDBOX
def test_get_statuses(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.get_api_settings_statuses_auto()


@allure.id("79669")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление статусами пользователя")
@allure.title(
    "Обновление списка автостатусов",
)
@SANDBOX
def test_post_statuses(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.post_api_settings_statuses_auto(
            [
                {
                    "media": "🤦",
                    "duration": 3600,
                    "text": {
                        "en": "facepalm",
                        "ru": "фейспалм",
                    },
                },
                {
                    "media": "🤦",
                    "name": "inCall",
                    "duration": 3600,
                    "text": {
                        "en": "facepalm",
                        "ru": "фейспалм",
                    },
                },
            ]
        )
