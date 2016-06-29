#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, Blueprint
from robot_helper.template_generator.controllers import convert_case_name, split_doc, parse_doc_lines_to_log_lines
from robot_helper.template_generator.forms import CaseInfoForm

__author__ = 'David Qian'

"""
Created on 06/01/2016
@author: David Qian

"""


profile = Blueprint('template_generator', __name__, template_folder='templates')


@profile.route('/file_template', methods=['POST', 'GET'])
def file_template():
    form = CaseInfoForm(request.form)
    if request.method == 'GET':
        return render_template('file_template.html', form=form)
    elif request.method == 'POST':
        if form.case_name.data:
            cvt_case_name = convert_case_name(form.case_name.data)
            robot_file_name = cvt_case_name + '.robot'
        else:
            cvt_case_name = None

        suite_doc, _ = split_doc(form.suite_doc.data, prefix='...    ')
        case_doc, origin_case_doc = split_doc(form.case_doc.data, prefix='    ...    ')
        log_lines = parse_doc_lines_to_log_lines(origin_case_doc)

        if not suite_doc:
            suite_doc = ['']

        if not case_doc:
            case_doc = ['']

        return render_template('file_template_result.html', **locals())
