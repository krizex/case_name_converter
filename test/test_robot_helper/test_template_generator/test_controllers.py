#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from robot_helper.template_generator.controllers import convert_case_name

__author__ = 'David Qian'

"""
Created on 06/28/2016
@author: David Qian

"""


class TestConverter(unittest.TestCase):
    def test_convert(self):
        case_name = 'untagged dscp add ctag'
        cvt_name = convert_case_name(case_name)
        self.assertEqual(cvt_name, 'tc_untagged_dscp_add_ctag')
