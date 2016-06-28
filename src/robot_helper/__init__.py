#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for
from robot_helper.template_generator.views import profile as template_generator

__author__ = 'David Qian'

"""
Created on 06/28/2016
@author: David Qian

"""


app = Flask(__name__)

app.register_blueprint(template_generator)

@app.route('/')
def index():
    return redirect('/file_template')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
