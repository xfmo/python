#!/usr/bin/env python
#-*-coding:utf8-*-
"""
download common
basic functions
"""
import time
import os
import sys
import urllib, urllib2


def rec_time(func):
    def _rec_time(*args, **kwargs):
        try:
            start_time = time.time()
            return func(*args, **kwargs)
        finally:
            print 'total time', time.time() - start_time
    return _rec_time

def urlcallback(a, b, c):
    """
    callback
    """
    prec = 100.0*a*b/c
    if 100 < prec:
        prec = 100
    print "%.2f%%" % (prec,)

def get_content(url):
    """
    获得页面的内容
    """
    req = urllib2.Request(url, headers={'User-Agent':'Magic Browser'})
    return urllib2.urlopen(req).read()

def get_size(path):
    """
    reutrn file size by kb
    """
    return str(os.path.getsize(path)/1024) + 'kb'

def download(url_list, save_path):
    """
    下载文件，需要传递要下载文件的地址，以及要保存的位置
    url_list为list 格式为[{'url':'','name':''},……]
    save_path 为要保存文件的地址，如果不存在则创建
    """
    if not os.path.exists(save_path):
        os.path.makedirs(save_path)
    for url in url_list:
        path = os.path.join(save_path,url['name'])

        start_time = time.time()
        if os.path.exists(path):
            print>>sys.stdout, '已经存在', path
            continue
        else:
            try:
                urllib.urlretrieve(url['url'], path)
                print>>sys.stdout, '下载完成', url['name'], get_size(path), time.time() - start_time
            except:
                print>>sys.stderr, 'download error', url['name'], url['url']
