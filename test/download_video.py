#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib2
import urllib
import re,os
import time

# time
def rec_time(func):
    def _rec_time(*args):
        pre_time=time.time()
        f=func(*args)
        print 'start time:',pre_time,'\tend time:',time.time(),'\ttotal:',time.time()-pre_time
        return f
    return _rec_time
#callback
def urlcallback(a,b,c):
    print "callback"
    prec=100.0*a*b/c
    if 100<prec:
        prec=100
    print "%.2f%%"%(prec,)
#get and download file
@rec_time
def download(url,save_path):
    if not os.path.exists(save_path):
        print 'have no this path:'+save_path
        return
    req=urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage=urllib2.urlopen(req).read()
    href_com=re.compile("""(http://.*?.flv)""")
    name=re.compile("""<h1 id="videoTitle">(.*?)</h1>""")
    href_list=href_com.findall(webpage)
    file_name=name.findall(webpage)
    print href_list,file_name
    for href in href_list:
        if  href.find("""http://""")==0:
            try:
                #:urllib.urlretrieve(href,os.path.join(save_path,file_name[0]+'.flv'))
              print file_name
            except:
               print "cannot download this image :"+href
        else:
            print  href+"is not a right url"
#get url in  page
def get_page(url):
    page_url=[]
    req=urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage=urllib2.urlopen(req).read()
    href_com=re.compile("""(http://www.yinyuetai.com/video/\d+)""")
    href_list=href_com.findall(webpage)
    for href in href_list:
     if href.find("""http://""")==0:
         page_url.append(href)
    return list(set(page_url))
if __name__=="__main__":
    page_url=raw_input('page_url->')
    page= get_page(page_url)
    save_path=raw_input('save_path->')
    for href in page:
        download(href,save_path) 
