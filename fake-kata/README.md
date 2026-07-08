Запуск

`docker run -d -p 80:80 registry-gitlab.corp.mail.ru/v.korobov/fake-kata:latest`

Использование с docker-compose

```
git clone git@gitlab.corp.mail.ru:v.korobov/fake-kata.git
cd fake-kata
sudo bash init-letsencrypt.sh URL
docker-compose up -d
```

Параметры задаются через env в docker-compose.yml

Swagger - https://host:port/docs
