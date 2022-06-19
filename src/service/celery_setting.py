from __future__ import absolute_import, unicode_literals
from celery import Celery


app = Celery(
    'service',
    broker="pyamqp://guest@localhost",
    backend="rpc://guest@localhost",
    include=['src.service.get_items_url_service']
)


if __name__ == '__main__':
    app.start()