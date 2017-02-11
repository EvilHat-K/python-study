#!/usr/bin/env python
# -*-coding:utf8 -*-

import json, sys

if(len(sys.argv) == 1):
    print 'Usage: python json_parse.py jsonfile'
    quit()


json_file = sys.argv[1]
f = open(json_file)
f = json.load(f) #这里注意下, 如果是从文件里读取json数据, 那么这里应该用load方法, 如果是字符就用loads 
for num in f:
    try:
        target =  num['target']  #防止某些数据没有值导致输出不完整
    except Exception, e:
        target = ''

    try:
    	ip = num['plugins']['IP']['string'][0]
    except Exception, e:
    	ip = ''

    try:
    	httpserver = num['plugins']['HTTPServer']['string'][0]
    except Exception, e:
    	httpserver = ''

    print target+','+ip+','+httpserver
