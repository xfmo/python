#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
def read_data(filename):
    '''读取文件'''
    lines=[]
    fh=None
    try:
        fh=open(filename)
        for line in fh:
            lines.append(line)
    except IOError  as err:
            print(err)
            return []
    finally:
            if fh is not None:
                fh.close()
    return lines
#renage 
def rangetest():
    #不包括5
    for i in range(1,5):
        print i
    print '======' #第三个参数跳步
    for k in range(1,5,2):
        print k
def operationtest():
    print 4/3
    print 4/3.0
    print 4//3.0
def systest():
    for i in sys.argv:
        print i
    for  k in sys.path:
        print k
def dicttest():
    data={'zhangsan':'abc@113.com',
            'lisi':'lisi@163.com' 
         }
    print data
    data['wangwu']='wangwu@courade.com'
    if 'wangwu' in data: # or data.has_key('wangwu')
        print data['wangwu']
def strtest():
    name="this is my first string test"
    if name.startswith('th'):
        print 'yes ,this string is start width "th"'
    if 'is' in name:
        print 'yes it contains the string "is"'
    if name.find('my'):
        print 'yes ,it contains the string "my"'
    mylist=['courade','99du']
    delimiter='-*-'
    print delimiter.join(mylist)
    print ''.join(mylist)
if __name__=='__main__':
    strtest()
    dicttest() 
    #print '%s is %d years old ' %('courade',25)
    #systest()
    #print read_data.__doc__
    #rangetest()
    #operationtest()
    #获取文件
    #data=read_data('/home/xfmo/puzhi/const.py')
    #print data
    margin=True
    width=100+(10 if margin else 0)
    #width=100
   # print sys.platform.startswith("linux2")
    # while 循环
    i=10
    while i<10:
        print i
        i=i+1
    else:
        print "end"

