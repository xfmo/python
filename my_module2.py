#! /usr/bin/python
# -*-coding:utf-8-*-
import my_module
#import os
print "this is second module"
print __name__
my_module.say_hello()
if __name__=="__main__":
   print dir(__name__)
   print os.listdir(os.getcwd())
