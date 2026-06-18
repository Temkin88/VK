# Установка зависимостей

- Получаем доступ в группу imqa
- Выпускаем access token для доступа в gitlab
- Добавляем дополнительные индексы в pip
```bash
venv .venv
source .venv/bin/activate
export GITLAB_TOKEN="YOUR_GITLAB_TOKEN"
pip config set global.extra-index-url "https://__token__:${GITLAB_TOKEN}@gitlab.corp.mail.ru/api/v4/projects/24781/packages/pypi/simple https://__token__:${GITLAB_TOKEN}@gitlab.corp.mail.ru/api/v4/projects/31236/packages/pypi/simple https://__token__:${GITLAB_TOKEN}@gitlab.corp.mail.ru/api/v4/projects/27355/packages/pypi/simple https://__token__:${GITLAB_TOKEN}@gitlab.corp.mail.ru/api/v4/projects/28233/packages/pypi/simple https://__token__:${GITLAB_TOKEN}@gitlab.corp.mail.ru/api/v4/projects/25444/packages/pypi/simple"
```
- Устанавливаем зависимости
```bash
source .venv/bin/activate
pip install .
```

# Запуск тестов

Смотреть https://confluence.vk.team/pages/viewpage.action?pageId=918741198