#!/usr/bin/env python
#-*- coding:utf-8 -*-
#对参数不确定的函数进行装饰
def deco(func):
    def _deco(*args,**kwargs):
        print("before %s called " % func.__name__)
        if 'd' in kwargs.keys():
            kwargs['d']+=" append"

        print '参数',args,kwargs
        ret=func(*args,**kwargs)
        print("after %s called " % func.__name__)
        print ret
        return ret
    return _deco
@deco
def myfunc(a,b):
    print("myfunc(%s,%s) called " %(a,b))
    return a+b
@deco
def myfunc2(a,b,c,**kwargs):
    print("myfunc(%s,%s,%s) called " %(a,b,c))
    print 'function2', kwargs
    return a+b+c

print myfunc(1,3)
myfunc2(1,3,4,d="this is test")
