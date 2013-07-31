#!/usr/bin/env python
#-*-coding:utf-8-*-

#学习网址http://blog.csdn.net/cain/article/details/6605705  
import threading
import time

def context(tJoin):
    print 'in threadContext'
    tJoin.start()
    tJoin.join() #将阻塞tContext直到tmyJoin终止
    print 'out threadContext'

def myJoin():
    print 'in myJoin'
    time.sleep(3)
    print 'out myJoin'

tmyJoin = threading.Thread(target=myJoin)
tContext = threading.Thread(target=context, args=(tmyJoin,))

tContext.start()
