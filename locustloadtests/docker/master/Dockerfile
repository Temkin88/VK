FROM mirror.gcr.io/python:3.12-bullseye

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./base ./base
COPY ./scenarios ./scenarios
COPY ./base_new ./base_new
COPY ./scenarios_new ./scenarios_new
COPY ./pyvkteamsclient ./pyvkteamsclient
COPY ./conf/master.conf ./locust.conf
COPY ./locustfile.py ./locustfile.py
COPY ./locust_tasks.py ./locust_tasks.py
