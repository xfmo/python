#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
def rectime(func):
    def _rectime(x):
        pretime=time.time()
        print pretime
        f=func(x)
        print time.time()
        print( time.time()-pretime)
        return f
    return _rectime


f=lambda x : x and x +f(x-1)  or 1
@rectime
def lambdatest(num):
    print(f(num))
@rectime
def show(n):
    for i in range(n):
        print i

f=open('/home/xfmo/helloworld.py','a')
f.write("jjflsdjflsdfjlfjsldjfsdlkkk")
print f
f.close()
file=open('/home/xfmo/helloworld.py','r')
print file.readline()
#lambdatest(900)
#显示对象的所有属性
#print dir([])
