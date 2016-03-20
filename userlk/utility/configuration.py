# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Maxim Kolyubyakin'

def load_configuration(app):
    app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
    app.config['CELERY_RESULT_BACKEND'] = 'amqp://guest:guest@localhost:5672//'
