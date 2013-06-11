#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import time

source=['/test1/puzhi','/test1/my_python_test']
target_dir='/test/backup/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
print  ' '.join(source)
#os.system("sudo touch %s" % target)
zip_command="sudo zip -qr '%s' %s" % (target,' '.join(source))
if os.system(zip_command)==0:
    print 'Successful backup to ',target
else:
    print 'backup failed'
