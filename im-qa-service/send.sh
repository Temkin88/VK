curl -X POST 'https://api.internal.myteam.mail.ru/bot/v1/messages/sendFile' -k -vvv \
	-F 'token=001.2177161926.0690735952:1000001281' \
	-F 'chatId=v.korobov@corp.mail.ru' \
	-F file=@$1
