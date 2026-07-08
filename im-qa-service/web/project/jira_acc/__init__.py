import aiojira

from web.project.jira_acc.constants import private_key


async def get_jira():
    return await aiojira.JIRA.create(
        options={
            "server": "https://jira.vk.team"
        },
        oauth={
            'access_token': '1FiifswDIuZPuRBlMZsGBI70qEOPmhkl',
            'access_token_secret': '5H0CX6PNzwrUFN4YHfDe8LC4Qz5W7ARX',
            'consumer_key': 'Oa3xK77mfYkg7oSz',
            'key_cert': private_key
        }
    )
