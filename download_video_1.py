#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib2
import urllib
import re,os
import time
import sys


def rec_time(func):
    """
    记录运行时间
    """
    def _rec_time(*args):
        pre_time = time.time()
        f = func(*args)
        print 'start time:',pre_time,'\tend time:',time.time(),'\ttotal:',time.time()-pre_time
        return f
    return _rec_time

def urlcallback(a, b, c):
    """
    callback
    """
    prec = 100.0*a*b/c
    if 100 < prec:
        prec = 100
    print "%.2f%%" % (prec,)

def getsize(path):
    """
    return file size by kb
    """
    return str(os.path.getsize(path)/1000)+' kb'

@rec_time
def download(url_list, save_path):
    """
    下载文件，需要传递要下载文件的地址，以及要保存的位置
    url_list为list 格式为[{'url':'','name':''},……]
    save_path 为要保存文件的地址，如果不存在则创建
    """
    start_time = time.time()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for url in url_list:
        name = os.path.join(save_path, url['name'])
        if os.path.exists(name):
            print>>sys.stdout, '已经存在 ', name, getsize(name), time.time() - start_time
            continue
        else:
            try:
                urllib.urlretrieve(url['url'], name)
                print>>sys.stdout, '下载完成', name, getsize(name), time.time() - start_time
            except:
                print>>sys.stdout, 'downlad error'

def get_content(url):
    """
    获取匹配网页的内容
    """
    req = urllib2.Request(url, headers={'User-Agent':'Magic Brower'})
    webpage = urllib2.urlopen(req).read()
    return webpage

def get_url(url_list):
    """
    根据url获取页面中视频的地址
    并将结果放在download_url中，并返回
    """
    download_url = []
    for u in url_list:
        webpage = get_content(u)
        href_com = re.compile("""(http://.*?.flv\?sc=.*?=\d+)""")
        href_list = href_com.findall(webpage)
        name = re.compile("""<meta property="og:title" content="(.*?)"/>""")
        file_name = name.findall(webpage)
        if href_list and file_name:
            if href_list[0].find("""http://""") == 0:
                download_url.append({'url':href_list[0],'name':file_name[0]+'.flv'})
        else:
            print>>sys.stderr, "没有匹配的内容", u
    return download_url

def read_url(path):
    """
    read file for url
    """
    urls = []
    f_handler = open(path, 'r')
    for line in f_handler.readlines():
        if line != '\n':
            urls.append(line.strip('\n'))
    return urls


if __name__ == "__main__":

    url_list = read_url('/home/xfmo/yinyuetai.txt')
    for i in range(100):
        url_data = get_url(url_list)
        if url_data != None:
            break;
        else:
            time.sleep(5)
    #print>>sys.stdout, '下载内容', url_data
    download(url_data,'/media/disk_01/video')
    #os.system('shutdown -h +1') # 一分钟后关机，要sudo运行
