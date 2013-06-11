#!/usr/bin/env python 
# -*-coding:utf-8-*-


def deco(func):
    def _deco():
        print("before myfunc() called")
        func()
        print("after myfunc() called")
    return  _deco
@deco
def myfunc():
    print("myfunc() called")
    return 'ok'

#myfunc=deco(myfunc)
myfunc()
myfunc()
