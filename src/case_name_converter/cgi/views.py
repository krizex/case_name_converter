#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

from case_name_converter.converter.converter import convert_case_name

__author__ = 'David Qian'

"""
Created on 06/01/2016
@author: David Qian

"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/case_name_convert', methods=['POST', 'GET'])
def case_name_convert():
    case_name = request.args.get('case_name')
    if case_name:
        cvt_name = convert_case_name(case_name)
        cvt_name += '.robot'
    else:
        cvt_name = 'invalid case name'

    return render_template('index.html', case_name=case_name, converted_name=cvt_name)


if __name__ == "__main__":
    app.run(host='0.0.0.0')