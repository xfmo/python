#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
"""
#python
import urllib2
import urllib
import re,os
import time
import sys

#local
from download_common import * 


def get_url(url_list):
    """
    根据url获取页面中视频的地址
    并将结果放在download_url中，并返回
    """
    download_url = []
    for u in url_list:
        webpage = get_content(u)
        #print webpage
        href_com = re.compile("""(http://.*?.flv\?sc=.*?=\d+)""")
        href_list = href_com.findall(webpage)
        #name = re.compile("""<meta property="og:title" content="(.*?)">""")
        name = re.compile("""title : \"(.*?)\"""")
        file_name = name.findall(webpage)
        print href_list, file_name
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
        print url_data
        if url_data != None:
            break;
        else:
            time.sleep(5)
    #print>>sys.stdout, '下载内容', url_data
    download(url_data,'/media/disk_01/video')
    #os.system('shutdown -h +1') # 一分钟后关机，要sudo运行
