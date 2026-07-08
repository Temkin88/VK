"""
Константы для работы метрик
"""

with open('./jira_privatekey.pem') as f:
    data = f.read()
privateKeyString = data.strip()

JIRA_CRED = {
    "server": "https://jira.vk.team",
    "oauth": {
        'access_token': '1FiifswDIuZPuRBlMZsGBI70qEOPmhkl',
        'access_token_secret': '5H0CX6PNzwrUFN4YHfDe8LC4Qz5W7ARX',
        'consumer_key': 'Oa3xK77mfYkg7oSz',
        'key_cert': privateKeyString
    }
}

CRED = {
    "token": "002.1632236290.4245359401:1000000391",
    "api_url_base": "https://api.internal.myteam.mail.ru/bot/v1"
}

AUTO_SEARCH_KEY = "project = {projects} " \
             "AND 'auto QA Complexity' = {value} " \
             "AND 'QA Complexity' IN (NULL, EMPTY) " \
             "AND status NOT IN (Закрыт, Closed) " \
             "AND issuetype IN (Уязвимость, Bug, Task) " \
             "ORDER BY issuekey DESC"

MANUAL_SEARCH_KEY = "project = {projects} " \
             "AND 'QA Complexity' = {value} " \
             "AND status NOT IN (Закрыт, Closed) " \
             "AND issuetype IN (Уязвимость, Bug, Task) " \
             "ORDER BY issuekey DESC"
