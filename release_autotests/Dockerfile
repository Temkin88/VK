FROM registry-gitlab.corp.mail.ru/imdevops/imhub/images/python:3.12 AS build

ENV WORKDIR=/workdir
WORKDIR $WORKDIR

ENV VIRTUAL_ENV=$WORKDIR/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PIP_TRUSTED_HOST="pypi.org gitlab.corp.mail.ru"
ENV PIP_INDEX_URL="https://pypi.org/simple/"
ENV PIP_EXTRA_INDEX_URL="https://__token__:9sB-zvU818WmFwkXechX@gitlab.corp.mail.ru/api/v4/groups/3011/-/packages/pypi/simple"

ENV PYTHONWARNINGS="ignore"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./tests/__init__.py $WORKDIR/tests/__init__.py
COPY ./pyproject.toml $WORKDIR

# hadolint ignore=DL3013
# hadolint ignore=SC1091
RUN apt-get update && \
    apt-get install --no-install-recommends -yy \
    wget=1.21.3-1+deb12u1 && \
    pip install virtualenv==20.23.0  --no-cache-dir --quiet && \
    virtualenv $VIRTUAL_ENV && \
    $VIRTUAL_ENV/bin/python -m pip install --upgrade pip==23.1.2 --no-cache-dir --quiet --require-virtualenv && \
    $VIRTUAL_ENV/bin/python -m pip install . --no-cache-dir --require-virtualenv && \
    wget  --progress=dot:giga https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_linux_386 -O /usr/bin/allurectl


FROM registry-gitlab.corp.mail.ru/imdevops/imhub/images/python:3.12

ENV WORKDIR=/workdirlogin_admin
WORKDIR $WORKDIR

ENV TZ=Europe/Moscow

ARG ALLURE_TOKEN
ENV ALLURE_TOKEN=$ALLURE_TOKEN
ENV ALLURE_ENDPOINT=https://allure.vk.team
ENV ALLURE_PROJECT_ID=7
ENV ALLURE_LAUNCH_NAME="SANDBOX ($(hostname)) | $(date)"
ENV ALLURE_LAUNCH_TAGS=SANDBOX,night_release,docker,puppet
ENV ALLURE_RESULTS=$WORKDIR/reports

ENV PUPPET_TESTS=true

ENV PYTHONWARNINGS="ignore"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


ENV VIRTUAL_ENV=$WORKDIR/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=build $VIRTUAL_ENV $VIRTUAL_ENV
COPY --from=build --chown=root /usr/bin/allurectl /usr/bin

# hadolint ignore=DL3008,DL3009,DL3018
RUN apt-get update && \
    apt-get install --no-install-recommends -yy \
    curl=7.88.1-10+deb12u14 \
    libasound2-dev=1.2.8-1+b1 \
    libgbm-dev=22.3.6-1+deb12u1 \
    libxrandr2=2:1.5.2-2+b1 \
    libxfixes-dev=1:6.0.0-2 \
    libxdamage-dev=1:1.1.6-1 \
    libxcomposite-dev=1:0.4.5-1 \
    libxkbcommon-dev=1.5.0-1 \
    libdbus-1-dev=1.14.10-1~deb12u1 \
    libdrm-dev=2.4.114-1+b1 \
    libcups2=2.4.2-3+deb12u8 \
    libatk-bridge2.0-0=2.46.0-5 \
    libnspr4=2:4.35-1 \
    libnss3=2:3.87.1-1+deb12u1 \
    libatk1.0-dev=2.46.0-5 \
    jq=1.6-2.1+deb12u1 && \
    chmod 755 /usr/bin/allurectl

COPY .  .

ENTRYPOINT [ "/bin/sleep", "infinity" ]
