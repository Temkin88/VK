# IM QA Helper

### Это вспомогательный сервис для автотестов ICQ/VK Teams

## 1. Start

```bash
git clone git@gitlab.corp.mail.ru:imqa/im-qa-helper.git
cd im-qa-helper
mkdir Attention
mkdir Difference
mkdir Origins
docker-compose up -d --build
```

## 2. Документация по методам сервиса доступна по следующим URL

http://(ip or domain)/docs - Swagger
http://(ip or domain)/redoc - Redoc

## 3. Просмотр логов запущенных сервисов

```bash
docker-compose logs -f [SERVICE_NAME] - логи отдельного сервиса
или
docker-compose logs -f - сводные логи сервисов
```