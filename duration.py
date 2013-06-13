#!/usr/bin/env python
#-*-coding:utf-8-*-
import time
from test import pystone
benchtimes,pystones=pystone.pystones()
#将消耗时间转化为pystones数
def seconds_to_pystones(seconds):
    return (pystones*seconds)
stats= {}
def duration(name='stats',stats=stats):
    def _duration(func):
        def __duration(*args,**kw):
            start_time=time.time()
            try:
                return func(*args,**kw)
            finally:
                total=time.time()-start_time
                kstones=seconds_to_pystones(total)
                stats[name]=total,kstones
        return __duration
    return _duration
@duration()
def mytest():
    print 'ok'
if __name__=="__main__":
    mytest()
    print stats

