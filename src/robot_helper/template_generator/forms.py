#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, StringField, TextAreaField

__author__ = 'David Qian'

"""
Created on 06/29/2016
@author: David Qian

"""


class CaseInfoForm(Form):
    case_name = StringField('Case Name:')
    author_name = StringField('@author:')
    tcid = StringField('@TCID:')
    suite_doc = TextAreaField('Suite Documentation:', default='Please fill test suite documentation.')
    case_doc = TextAreaField('Case Documentation:', default='Please fill test case documentation.')
