#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
def deco(func):
    def _deco(a,b):
        print("before myfunc called")
        ret=func(a,b)
        print("after myfunc called")
        return ret
    return _deco
@deco
def myfunc(a,b):
    print("myfunc(%s,%s) called" % (a,b))
    return a+b;
print myfunc(1,2)
myfunc(2,3)
