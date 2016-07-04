#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, render_template, Blueprint, make_response
from robot_helper.template_generator.controllers import convert_case_name, split_doc, parse_doc_lines_to_log_lines, \
    save_file_template, search_file_template
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
            return render_template('file_template_result.html', **locals())

        suite_doc, _ = split_doc(form.suite_doc.data, prefix='...    ')
        case_doc, origin_case_doc = split_doc(form.case_doc.data, prefix='    ...    ')
        log_lines = parse_doc_lines_to_log_lines(origin_case_doc)

        if not suite_doc:
            suite_doc = ['']

        if not case_doc:
            case_doc = ['']

        case_setup_name = form.tcid.data + ' setup' if form.tcid.data else 'case setup'
        case_teardown_name = form.tcid.data + ' teardown' if form.tcid.data else 'case teardown'

        robot_file_stream = render_template('template.robot', **locals())

        file_id = save_file_template(robot_file_name, robot_file_stream)
        file_link = '/'.join(['http://' + request.host, 'download_file', file_id])

        return render_template('file_template_result.html', **locals())


@profile.route('/download_file/<file_id>', methods=['GET'])
def download_file(file_id):
    try:
        ret = search_file_template(file_id)
    except KeyError:
        return 'Invalid file id %s' % file_id

    content = ret[1]
    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=%s" % (ret[0])
    return response
