#! /usr/bin/env python
# -*-coding:utf-8 -*-
import os
rootdir='/home/xfmo/my_python_test/'
print rootdir
for file in os.listdir(rootdir):
    print file
    if os.path.isfile(file):
       f=open(file)
      # print f.readlines()
def readfile(path):
    f=open(path)
    for l in f.readlines():
        print l
    f.close()
if __name__=="__main__":
    readfile(os.path.join(rootdir,'lambda.py'))
