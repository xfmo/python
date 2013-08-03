#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2
import urllib
import re,os
import time
import json

start_time = time.time()
def get_page(url):
    download_url = []
    req = urllib2.Request(url, headers={'User-Agent':'Magic Browser'})
    webpage = urllib2.urlopen(req).read()
    try:
        data = json.loads(webpage.replace("'","\""))
    except:
        data = json.loads(webpage)
    for li in data['data']['list']:
        pdf = li['thumb'].replace("_thumb.jpg",'.pdf')
        download_url.append({'url':pdf,'title':li['title']})
    return download_url


def download(url_list,save_path):

    if not os.path.exists(save_path):
        os.mkdir(save_path)
        #print 'the system has no this path'+save_path
        return

    for url in url_list:
        start_time = time.time()
        path = os.path.join(unicode(save_path,'utf-8'),url['title'].replace('/','-') + '.pdf')
        #print '下载',url['url']
        try:
            #print 'ok'
            urllib.urlretrieve(url['url'],path)
        except:
            print 'error'

        print '下载完成',path,time.time() - start_time,'大小:',os.path.getsize(path)/1024 , time.time(), start_time
if __name__ == "__main__":
    url_list = []
    for i in range(1,20):
        url_list = (get_page('http://share.csdn.net/api/csdnshare/list/pageno/'+str(i)+'/pagesize/19/format/json/'))
        download(url_list,'/media/视频及资料/csdn_pdf/'+str(i))
        #print i ,len(url_list)


