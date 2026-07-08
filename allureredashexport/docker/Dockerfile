FROM mirror.gcr.io/python:3.13-bullseye AS build

WORKDIR /workdir

ENV VIRTUAL_ENV=/workdir/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PYTHONWARNINGS="ignore"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache-dir --require-virtualenv

FROM mirror.gcr.io/python:3.13-bullseye

WORKDIR /workdir

ENV VIRTUAL_ENV=/workdir/venv

COPY --from=build /workdir/venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PYTHONWARNINGS="ignore"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./project /workdir/project
COPY ./common /workdir/common