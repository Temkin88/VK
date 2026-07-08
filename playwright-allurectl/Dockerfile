ARG FROM_VERSION_TAG=20.17-bullseye
ARG PW_VERSION=v1.46.1

FROM mirror.gcr.io/node:${FROM_VERSION_TAG}

WORKDIR /project

ENV TZ=Europe/Moscow
ENV ALLURE_ENDPOINT=https://allure.vk.team
ENV ALLURE_PROJECT_ID=8
ENV ALLURE_RESULTS="allure-results"

RUN apt-get update && \
    apt-get install -yy lsof jq wget --no-install-recommends && \
    apt-get clean &&  \
    rm -rf /var/lib/apt/lists/* && \
    npm install "playwright@$PW_VERSION" && \
    npx playwright install --with-deps && \
    npx playwright install chrome && \
    wget --progress=dot:giga https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_linux_386 -O /usr/local/bin/allurectl && \
    chmod +x /usr/local/bin/allurectl && \
    wget --progress=dot:giga https://dl.filippo.io/mkcert/latest?for=linux/amd64 -O /usr/local/bin/mkcert && \
    chmod +x /usr/local/bin/mkcert

CMD ["bash"]