#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import time

source=['/home/test1/puzhi','/home/test1/my_python_test']
target_dir='/home/test/backup/'
today=target_dir+time.strftime('%Y%m%d')
now=time.strftime("%H%M%S")
#create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) #make directory
    print 'Successfully created directory ', today
#target:::
target=today+os.sep+now+'.zip'

#os.system("sudo touch %s" % target)
zip_command="sudo zip -qr '%s' %s" % (target,' '.join(source))
if os.system(zip_command)==0:
    print 'Successful backup to ',target
else:
    print 'backup failed'
