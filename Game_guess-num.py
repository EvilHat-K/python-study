#!/usr/bin/env python
# -*- coding=utf-8 -*-

import random

print "这是一个小游戏,猜数字的小游戏根据提示你只要输入就可以了^_^!!"
rand = random.randint(0,99)
#cai = raw_input('请输入一个数字100以内哦!: ')
errorh = "猜错了,大了,继续,大SB"
errorl = "猜错了,小了,继续,小SB"
suecc = "恭喜你猜对了,NB!"
while 1:
    cai = raw_input('请输入一个数字100以内哦!: ')
    cai = int(cai)  #这里需要转换数据类型,不然比较是会出错
    if cai > rand:
        print(errorh)
    elif cai < rand:
        print(errorl)
    elif cai == rand:
	print(suecc)
        quit()
