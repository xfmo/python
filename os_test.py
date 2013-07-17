#!/usr/bin/env python
#-*-conding:utf-8-*-

import os

def main(path):
   #path = os.getcwd()
    dirs = os.listdir(path)
    for d in dirs:
        file_path = path+"/"+d
        if os.path.isfile(file_path):
            print file_path, os.path.getsize(file_path)/1024
        elif os.path.isdir(file_path):
            main(file_path)
           
if __name__=="__main__":
    main(os.getcwd())
    
