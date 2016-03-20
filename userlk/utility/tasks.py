# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

__author__ = 'Maxim Kolyubyakin'

from celery import Celery
from userlk.main import app

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

@celery.task
def add(x, y):
    return x + y

result = add.delay(23, 42)
result.wait()
