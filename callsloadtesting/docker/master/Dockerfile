FROM mirror.gcr.io/python:3.12-bullseye

# Получаем права суперпользователя
USER root

ENV PIP_TRUSTED_HOST="gitlab.corp.mail.ru"
ENV PIP_EXTRA_INDEX_URL="https://__token__:9sB-zvU818WmFwkXechX@gitlab.corp.mail.ru/api/v4/groups/3011/-/packages/pypi/simple"

# Устанавливаем пакет procps для команды ps
RUN apt-get update && apt-get install -y procps git

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./shape.toml .
COPY ./conf/master.conf ./locast.conf
COPY ./load.toml .
COPY ./common ./common
COPY ./scenario ./scenario
COPY ./locustfile.py .
COPY ./logging_config.py .
COPY ./config.yml .
COPY ./config_loader.py .
