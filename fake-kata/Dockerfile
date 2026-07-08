FROM registry-gitlab.corp.mail.ru/imqa/release_autotests/python:3.11-alpine
WORKDIR /code
COPY . .
RUN pip install --no-cache-dir --upgrade pip &&  \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
