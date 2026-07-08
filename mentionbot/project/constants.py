TOKEN = '002.0455033360.1988155478:1000002627'
API_URL = 'https://api.internal.myteam.mail.ru/bot/v1/'

LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '<green>{time:HH:mm:ss.SSS}</green> | type: {extra[event_type]: <27}  | <level>{level: <8}</level> | <cyan>{function: <27}</cyan>:<cyan>{line: <4}</cyan> | chat_id: {extra[chat_id]: <25} | user_id: {extra[user_id]: <25} | cmd: {extra[cmd_text]: <10} - <level>{message}</level>'

COMMANDS_LIST = ['/all', '/admin', '/start', '/stop', '/help']
HELP_TEXT = '''https://files-n.internal.myteam.mail.ru/get/0j8nY00009SLvmVpN2mD9A62b38fe91bb

Бот для групповых меншенов в группе

!!!ВАЖНО!!! Бот не меншенит отправителя команды и игнорирует других ботов в чате
!!!ВАЖНО!!! Бот не видит участников канала, пока не будет назначен в нем админом
        
Возможности:
/all - Прислать сообщение с меншенами всех членов группы

/{CUSTOM_GROUP_NAME} [MENTION...] - создание подгруппы, меншены которой будут вызываться в этом чате по команде /{CUSTOM_GROUP_NAME}, в группу будут добавлены все упомянутые в сообщении члены группы

/{CUSTOM_GROUP_NAME} - Прислать сообщение с меншенами членов подгруппы
/{CUSTOM_GROUP_NAME} [TEXT] - Прислать меншены с подписью TEXT

/admin - управление уже созданными подгруппами ваших чатов

По всем дополнительным вопросам и багам - обращаться к @[v.korobov@corp.mail.ru]
'''