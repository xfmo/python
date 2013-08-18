#!/usr/bin/env python 
#-*- coding:utf-8 -*-
def listtest():
    listone=[2,4,6,9,10]
    listtwo=[i*2 for i in listone if i>2]
    print listtwo
def powsum(power,*args):
    total=0
    for i in args:
        total+=pow(i,power)
    return total
if __name__=='__main__':
   print powsum(2,4,9)
    #listtest()

