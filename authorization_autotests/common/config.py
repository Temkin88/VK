import os

HOSTS_TEAMS = os.getenv("HOSTS_TEAMS", "vkt-auth-test.vkteams.vkwm.ru")
HOSTS_WS = os.getenv("HOSTS_WS", "auth-test.vkteams.vkwm.ru")

LOGIN_TEAMS_OTP = os.getenv("LOGIN_TEAMS_OTP", "autotest001@autotest.clients")
PASS_TEAMS_OTP = os.getenv("PASS_TEAMS_OTP", "ONPREM")
LOGIN_TEAMS_SSO = os.getenv("LOGIN_TEAMS_SSO", "10@clear-sso.auth-test.vkteams.vkwm.ru")
# LOGIN_TEAMS_SSO = os.getenv("LOGIN_TEAMS_SSO", "1@sso-real.auth-test.vkteams.vkwm.ru")
PASS_TEAMS_SSO = os.getenv("PASS_TEAMS_SSO", "12345")
LOGIN_TEAMS_SWA = os.getenv("LOGIN_TEAMS_OTP", "1@swadup.auth-test.vkteams.vkwm.ru")
PASS_TEAMS_SWA = os.getenv("PASS_TEAMS_SSO", "Oeoopr_YYU13")
LOGIN_WS = os.getenv("LOGIN_TEAMS_OTP", "admin@admin.qdit")
PASS_WS = os.getenv("PASS_TEAMS_SSO", "TF54sD6G68sjJM+K")

