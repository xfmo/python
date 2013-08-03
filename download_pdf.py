#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2
import urllib
import os
import time
import json
import shutil


def rec_time(func):
    """
    装饰器，统计时间
    """
    def _rec_time(*args, **kwargs):
        try:
            start_time = time.time()
            return func(*args, **kwargs)
        finally:
            print time.time() - start_time 
    return _rec_time

def get_page(url):
    """
    获得下载文件的路径
    """
    
    download_url = []
    req = urllib2.Request(url, headers={'User-Agent':'Magic Browser'})
    webpage = urllib2.urlopen(req).read()
    try:
        data = json.loads(webpage.replace("'","\""))
    except:
        data = json.loads(webpage)
    for li in data['data']['list']:
        pdf = li['thumb'].replace("_thumb.jpg",'.pdf')
        download_url.append({'url':pdf,'title':li['title'].replace('/','-')+'.pdf'})
    return download_url

def download(url_list, save_path):
    """
    下载文件，并保存
    
    """
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        #print 'the system has no this path'+save_path
        return
    for url in url_list:
        start_time = time.time()
        path = os.path.join(unicode(save_path,'utf-8'), url['title'])
        #print '下载',url['url']
        try:
            #print 'ok'
            urllib.urlretrieve(url['url'], path)
        except:
            print 'error'

        print '下载完成',path,time.time() - start_time,'大小:',os.path.getsize(path)/1024 , time.time(), start_time

@rec_time
def compare_pdf(url_list, save_path,copy_path):
    """
    入股已经下载了，但中间可能有丢失的情况，
    使用此方法可以从已经下载的文件中找到相关的文件
    ，然后判断是否要重新下载
    """
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for url in url_list:
        copy_file = os.path.join(unicode(copy_path), url['title'])
        if(os.path.exists(copy_file)):
            shutil.copyfile(copy_file,os.path.join(save_path, url['title']))
            print 'copy ok'
        else:
            print 'not exists'

if __name__ == "__main__":

    url_list = []
    for i in range(1, 20):
        url_list = (get_page('http://share.csdn.net/api/csdnshare/list/pageno/'+str(i)+'/pagesize/19/format/json/'))
        #download(url_list,'/media/视频及资料/csdn_pdf/'+str(i))
        #print i ,len(url_list)
        compare_pdf(url_list, '/media/media_document/csdn_pdf2/'+str(i), '/media/media_document/csdn_pdf2/copy')



