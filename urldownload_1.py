#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
    download 网易摄影图片
    #form download import download
    #http://pp.163.com/poki/pp/7816141.html
"""

#python
import urllib2
import urllib
import re,os

#local
from download_common import *

def test(url):
    req = urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage = urllib2.urlopen(req)
    html_line = webpage.readline()
    while html_line:
        if html_line.find('data-lazyload-src'):
            print html_line
        html_line=webpage.readline()
    #soup=BeautifulSoup(webpage.read())

def get_url(url):
    img_sum = 0
    webpage = get_content(url)
    href_com = re.compile("""<img.*?data-lazyload-src="(.*?)".*?>""")
    href_list = href_com.findall(webpage)
    for href in href_list:
        if  href.find("""http://""")==0:
            image_name = href[href.rindex('/')+1:]
            try:
               download([{"url":href,"name":image_name}],"/media/media_document/image")
               img_sum += 1
            except:
                print "cannot download this image :"+href
        else:
            print  href+"is not a right url"
    return img_sum

def get_page(url):
    page_url = []
    webpage = get_content(url)
    href_com = re.compile("""<a href="(.*?)" .*?>.*?</a> """)
    href_list = href_com.findall(webpage)
    for href in href_list:
     if href.find("""http://""")==0 and href.endswith('.html'):
         page_url.append(href)
    return page_url

if __name__=="__main__":
   url=['http://pp.163.com/poki/pp/9806131.html','http://pp.163.com/poki/pp/7570037.html']
   page=get_page('http://oldrabbit.pp.163.com/')
   count= len(page)
   for url in page:
       sum= get_url(url)
       print url,'页的图片数',sum
       count=count-1
       print '剩余页数', count
