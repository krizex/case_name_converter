#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, Blueprint
from robot_helper.template_generator.controllers import convert_case_name

__author__ = 'David Qian'

"""
Created on 06/01/2016
@author: David Qian

"""


profile = Blueprint('template_generator', __name__, template_folder='templates')


@profile.route('/file_template', methods=['POST', 'GET'])
def file_template():
    case_name = request.args.get('case_name')
    author_name = request.args.get('author_name', 'Unknown')
    tcid = request.args.get('tcid', 'Unknown')
    if case_name:
        cvt_case_name = convert_case_name(case_name)
        robot_file_name = cvt_case_name + '.robot'
    else:
        cvt_case_name = None

    return render_template('file_template.html', **locals())
