#! /usr/bin/env python
# -*-coding:utf-8 -*-
import os
rootdir='/home/xfmo/my_python_test/'
print rootdir
for file in os.listdir(rootdir):
    print file
    f=open(file)
    line=f.readline()
   # while line :
    #    print line
     #   line=f.readline()
