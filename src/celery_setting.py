from __future__ import absolute_import, unicode_literals
from celery import Celery


app = Celery(
    'src',
    broker="pyamqp://guest@3.34.5.27",
    include=['src.robot']
)

if __name__ == '__main__':
    app.start()
