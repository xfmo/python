#!/usr/bin/env python
#-*-conding:utf-8-*-

import os
file_dict = {}
def main(path):
   #path = os.getcwd()
    dirs = os.listdir(path)

    for d in dirs:
        file_path = path+"/"+d
        if os.path.isfile(file_path):
            file_dict["file_path"] = file_path
            file_dict["file_size"] = os.path.getsize(file_path)
            return file_dict
        elif os.path.isdir(file_path):
            main(file_path)
           
if __name__=="__main__":
    print main(os.getcwd())
    
