#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
    CSDN Share PPT下载
"""

import urllib2
import urllib
import os
import sys
import time
import json
import shutil

#local
from download_common import * 

def get_page(url):
    """
    获得下载文件的路径
    """
    download_url = []
    webpage = get_content(url)
    try:
        data = json.loads(webpage.replace("'","\""))
    except:
        data = json.loads(webpage)
    for li in data['data']['list']:
        pdf = li['thumb'].replace("_thumb.jpg",'.pdf')
        download_url.append({'url':pdf,'name':li['title'].replace('/','-')+'.pdf'})
    return download_url

@rec_time
def compare_pdf(url_list, save_path,copy_path):
    """
    如果已经下载了，但中间可能有丢失的情况，
    使用此方法可以从已经下载的文件中找到相关的文件
    ，然后判断是否要重新下载
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for url in url_list:
        copy_file = os.path.join(unicode(copy_path), url['title'])
        if(os.path.exists(copy_file)):
            shutil.copyfile(copy_file,os.path.join(save_path, url['title']))
            print>>sys.stdout, 'copy'+copy_file+'ok'
        else:
            print>>sys.stderr, 'not exists'

if __name__ == "__main__":
    url_list = []
    for i in range(1, 3):
        url_list = get_page('http://share.csdn.net/api/csdnshare/list/pageno/'+str(i)+'/pagesize/19/format/json/')
        download(url_list,'/media/media_document/csdn_pdf/'+str(i))
        #compare_pdf(url_list, '/media/media_document/csdn_pdf2/'+str(i), '/media/media_document/csdn_pdf2/copy')
