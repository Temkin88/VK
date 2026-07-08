from jira import JIRA


jira_account = JIRA(
    server='https://jira.vk.team',
    oauth={
        'access_token': '1FiifswDIuZPuRBlMZsGBI70qEOPmhkl',
        'access_token_secret': '5H0CX6PNzwrUFN4YHfDe8LC4Qz5W7ARX',
        'consumer_key': 'Oa3xK77mfYkg7oSz',
        'key_cert': '''-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC8zhttiR8vBj7Ki51Khw6aKKLWDmVJqHYNG3rsefXFlUOu9krM
4zyh1xMp3g+8nqTW9gCbYeq1GZ3BoTGWJA5kgj6eRrKGSj4G7CcdR8JP8QmbuzBo
Xhya/7XEnOrpR6lBIJ1O+jNvmDzT8ejoumYr9mdflIBTur/XrrHo/8n42QIDAQAB
AoGBAI/LRXZp/Zb54a6vIE9XhxZ/pmzyr8+mfqpC6J7b0AP4R4EkURm0Y0Q7Inw7
hK66AH87AoFU1MWyycRjuPlJYq93koY1dMjs29WQobFI43tCtTM5tpsVqwdKdKKK
Ub60MMFMdAhpqXH/CgZAsjFaUuS6QvnHHozWl6Bb0quFmYeVAkEA8EcB7zZUrjEU
gVB1RvIGfueHx1+UrBD87BYljkX1blAQm/yOzw6EtCJqJHap2gSNLleNPMwKm8jQ
94bGsfKq7wJBAMko3WmZvAPyzCnWnEvGKBDZttuVGgWa8Lte2SCK9tL51c6N9s77
uUlmOkDyhl780OvKmfr4uzkxHy7scP7quLcCQQCva7gO1ES4tB57Vql4tWRmrFTm
C3M4uGJfXr/mgk7wTcYCjD4bD0d1WBbULkpNYLtOVR9JftJT8CYYQS65ZijDAkBS
k4LosaI74LSszBuXA345BJaK51cqS+Ncl1/8eu89xi9dvms9ppn2Jo/tT2GXpqLA
2IeDPg3lOWP6qDbufj5bAkBbaUrj+nh2y6mx6KHbE7X1As+9SzrOcWMEhnELHMCu
lb9TnwKeTS5yasX/q9RcEexUyst6wO/u3iUfcHe8XCC2
-----END RSA PRIVATE KEY-----'''
    }
)

JIRA_PROJECTS_LIST = (
    'IMSUPPORT',
    'IMALL',
    'IMSERVER',
    'IMVOIP',
    'IMDESKTOP',
    'IMWEB',
    'IMA',
    'IMIOS',
    'TODO'
)

JIRA_ALL_UNASSIGNED_TASKS_JQL = 'project in ({projects}) AND resolution = Unresolved AND assignee is null ORDER BY updated DESC, priority DESC'.format(projects=','.join(JIRA_PROJECTS_LIST))

JIRA_ALL_ASSIGNED_ON_USER_TASKS_JQL = 'filter=131689 AND assignee in ({users}) ORDER BY updated DESC, priority DESC'

JIRA_EXPAND_FIELDS = 'status,assignee,project,priority,issuetype,aggregatetimeestimate,aggregatetimeoriginalestimate,customfield_18216,customfield_50606,customfield_50700'

JIRA_JQL_SEARCH_MAX_RESULTS = 1000
