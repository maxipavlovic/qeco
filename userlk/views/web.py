# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

__author__ = 'Maxim Kolyubyakin'

from flask import Blueprint

web_blueprint = Blueprint('web', __name__)

@web_blueprint.route("/")
def hello():
    return "Hello World!"
