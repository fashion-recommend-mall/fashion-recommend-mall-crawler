"""
This is celery files!

If you want to create celery worker,

Run this file with below code!

- Celery -A src.celery_setting worker -l INFO
"""
from __future__ import absolute_import, unicode_literals
from celery import Celery

from project_setting import celery_broker_url

broker_url : str = celery_broker_url["celery_broker_url"]

app = Celery(
    'src',
    broker=broker_url,
    include=['src.robot']
)

if __name__ == '__main__':
    app.start()
