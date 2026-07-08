FROM python:3.10.2-slim-buster

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code
COPY ./project /code/project

EXPOSE 80:80
CMD ["python", "main.py"]
