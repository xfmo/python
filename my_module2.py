#! /usr/bin/python
# -*-coding:utf-8-*-
import my_module as mod
print "this is second module"
print __name__
mod.say_hello()
if __name__=="__main__":
   print dir(__name__)
