#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time

import re

__author__ = 'David Qian'

"""
Created on 06/28/2016
@author: David Qian

"""

# replace special char in case name
REGEXP_CASE_NAME_SPEC_CHAR = re.compile(r'[^\w]+')

# replace all blank with one space
REGEXP_REPLACE_BLANK = re.compile(r'[ \t]+')


def convert_case_name(case_name):
    case_name = case_name.strip()
    if len(case_name) >= 3 and case_name[:3].upper() == 'TC_':
        pass
    else:
        case_name = 'tc_' + case_name
    cvt_name = REGEXP_CASE_NAME_SPEC_CHAR.sub('_', case_name)
    return cvt_name.strip('_')


def generate_robot_file_template(case_name):
    pass


def split_doc(doc, prefix='...    '):
    if doc is None:
        doc = ''
    origin_doc_list = doc.splitlines()
    parsed_doc_list = []
    first_line = True
    for line in origin_doc_list:
        if first_line:
            first_line = False
            parsed_doc_list.append(line)
            continue

        parsed_doc_list.append(prefix + line)

    return parsed_doc_list, origin_doc_list


def parse_doc_lines_to_log_lines(doc_lines):
    doc_lines = map(lambda x: REGEXP_REPLACE_BLANK.sub(' ', x).strip(), doc_lines)
    doc_lines = map(lambda x: 'log    STEP:' + x, doc_lines)
    return doc_lines


def save_file_template(file_name, file_content):
    from robot_helper import redis_store

    hash_key = generate_hash_key(file_name, file_content)
    d = {
        'file_name': file_name,
        'file_content': file_content,
    }
    ret = redis_store.hmset(hash_key, d)
    print ret
    return hash_key


def search_file_template(hash_key):
    from robot_helper import redis_store
    d = redis_store.hgetall(hash_key)
    return d['file_name'], d['file_content']


def generate_hash_key(*contents):
    time_stamp = time.localtime(time.time())
    time_str = time.strftime('%Y%m%d%H%M%S', time_stamp)
    algo = hashlib.md5()
    for c in contents:
        algo.update(c)
    hash_key = time_str + algo.hexdigest()
    return hash_key

