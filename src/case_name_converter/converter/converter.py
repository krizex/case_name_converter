#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

__author__ = 'David Qian'

"""
Created on 06/01/2016
@author: David Qian

"""


REOBJ = re.compile(r'[^\w]+')


def convert_case_name(case_name):
    if len(case_name) >= 3 and case_name[:3].upper() == 'TC_':
        pass
    else:
        case_name = 'tc_' + case_name
    return REOBJ.sub('_', case_name)




if __name__ == '__main__':
    pass