#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for
from flask.ext.redis import FlaskRedis
from robot_helper.template_generator.views import profile as template_generator

__author__ = 'David Qian'

"""
Created on 06/28/2016
@author: David Qian

"""


app = Flask(__name__)
app.jinja_env.trim_blocks = True

app.register_blueprint(template_generator)
redis_store = FlaskRedis(app)


@app.route('/')
def index():
    return redirect(url_for('template_generator.file_template'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
