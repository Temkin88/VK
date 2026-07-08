# Docker образ для запуска Playwright тестов

Образ для запуска автотестов на основе Playwright в проектах семейства IMWEB.

Используется в проектах:
- [VK Teams](https://gitlab.corp.mail.ru/web-im/icq)
- [Оргструктура](https://gitlab.corp.mail.ru/web-im/orgstructure)

Результаты прогонов тестов попадают в web интерфейс [Allure IMWEB](https://allure.vk.team/project/8/dashboards).

## Состав образа 

- [Playwright](https://playwright.dev/) с зависимостями своей работы;
- Свежие версии браузеров на момент сборки образа;
- [allurectl](https://docs.qameta.io/allure-testops/ecosystem/allurectl/) - инструмент для загрузки отчётов в Allure TestOps;

## Локальная сборка образа

1. Собрать образ, командой из папки репозитория:
```bash
docker build . -t registry-gitlab.corp.mail.ru/imqa/playwright-allurectl/playwright-allurectl:stable-20.17-bullseye
```

2. Загрузить на сервер:
```bash
docker push registry-gitlab.corp.mail.ru/imqa/playwright-allurectl/playwright-allurectl:stable-20.17-bullseye
```

## Сборка в облаке

* В меню репозитория найти [Build -> Pipelines](https://gitlab.corp.mail.ru/imqa/playwright-allurectl/-/pipelines);
* Запустить пайплайн;
* Собранные в CI образы сохраняются в [Deploy -> Container Registry -> playwright-allurectl](https://gitlab.corp.mail.ru/imqa/playwright-allurectl/container_registry/42966);

## Обновление версии базового образа 

Для этого необходимо сменить образ на основе которого собирается текущий в Dockerfile.

Новые версии образа можно найти [в документации к Playwright](https://mcr.microsoft.com/en-us/product/playwright/about).
