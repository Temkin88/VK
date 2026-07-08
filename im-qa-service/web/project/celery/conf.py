import os
import platform

from celery import Celery

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.celery import CeleryIntegration


sentry_sdk.init(
    "http://a147a3cbf86546fc8680ad931995d8bb@100.99.5.41:8000/3",
    traces_sample_rate=1.0,
    integrations=[
        CeleryIntegration(),
    ],
)

load_dotenv("../variables.env")


celery_app = Celery(__name__)
celery_app.conf.broker_url = os.getenv('CELERY_BROKER_URL') \
    if platform.system() != "Darwin" else "db+sqlite://db.sqlite"
celery_app.conf.result_backend = os.getenv('CELERY_RESULT_URL') \
    if platform.system() != "Darwin" else "db+sqlite://db.sqlite"
