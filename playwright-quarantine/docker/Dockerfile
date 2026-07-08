# syntax=docker/dockerfile:1.7

############################
# Stage 1: build venv + deps
############################
FROM python:3.14-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/.venv

WORKDIR /build

# Создаем venv
RUN python -m venv $VIRTUAL_ENV && \
    $VIRTUAL_ENV/bin/pip install -U pip && \
    $VIRTUAL_ENV/bin/pip install -U uv

ENV PATH="$VIRTUAL_ENV/bin:$PATH" \
    UV_PROJECT_ENVIRONMENT=$VIRTUAL_ENV \
    UV_LINK_MODE=copy

# Копируем только файлы зависимостей (для кеша слоев)
COPY pyproject.toml uv.lock ./

# Установка зависимостей в venv через uv sync
# --frozen: строго по lock
# --no-install-project: не ставим сам проект как пакет (нам достаточно исходников)
RUN uv sync --frozen --no-install-project --no-python-downloads

############################
# Stage 2: runtime
############################
FROM python:3.14-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/.venv

WORKDIR /app
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Копируем готовое виртуальное окружение
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

# Копируем только нужные файлы проекта
COPY app ./app
COPY qa_bot.py .
COPY alembic ./alembic
COPY alembic.ini ./alembic.ini
COPY pyproject.toml ./pyproject.toml

EXPOSE 8000

# По умолчанию запускаем API
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
