#!/usr/bin/env python
# -*- coding:utf-8 -*-

#此脚本生成4位a-z字典,循环生成了所有搭配方式的字符.
#如果要生成5位字典,再加一个循环就可以了

for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            for m in range(97,123):
                print 'mainrf'+chr(i)+chr(j)+chr(k)+chr(m)+'aspx'


