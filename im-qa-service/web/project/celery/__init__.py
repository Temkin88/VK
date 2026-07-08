import os

from datetime import datetime, timedelta

from celery.schedules import crontab

from web.project.celery.conf import celery_app
from web.project.logger import logger

import psycopg2

from requests import Session