#!/usr/bin/env python 
# -*-coding:utf-8-*-


def deco(func):
        print("before myfunc() called")
        func()
        print("after myfunc() called")
    return  func
@deco
def myfunc():
    print("myfunc() called")
    return 'ok'

#myfunc=deco(myfunc)

myfunc()
myfunc()
myfunc()
myfunc()
