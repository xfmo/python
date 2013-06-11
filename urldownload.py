#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib2
import urllib
import re,os
import time
#this is test
def test(url):
    req=urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage=urllib2.urlopen(req)
    html_line=webpage.readline()
    while html_line:
        if html_line.find('data-lazyload-src'):
            print html_line
        html_line=webpage.readline()
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
    img_sum=0
    req=urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage=urllib2.urlopen(req).read()
    href_com=re.compile("""<img.*?data-lazyload-src="(.*?)".*?>""")
    href_list=href_com.findall(webpage)
    for href in href_list:
        if  href.find("""http://""")==0:
            image_name=href[href.rindex('/')+1:]
            #print href, image_name
            try:
               #urllib.urlretrieve(href,os.path.join('/home/xfmo/my_python_test/image/',image_name),urlcallback)
               urllib.urlretrieve(href,os.path.join(save_path,image_name))
              # print image_name+" ok"
               img_sum+=1
            except:
                print "cannot download this image :"+href
        else:
            print  href+"is not a right url"
    return img_sum
#get url in  page
def get_page(url):
    page_url=[]
    req=urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage=urllib2.urlopen(req).read()
    href_com=re.compile("""<a href="(.*?)" .*?>.*?</a> """)
    href_list=href_com.findall(webpage)
    for href in href_list:
     if href.find("""http://""")==0 and href.endswith('.html'):
         page_url.append(href)
    return list(set(page_url))
if __name__=="__main__":
    page_url=raw_input('page_url>')
    page=get_page(page_url)#'h'http://oldrabbit.pp.163.com/') 'http://anqiink.pp.163.com/'
    for p in page:
        print p
    count= len(page)
    print 'total page',count
   
    save_path=raw_input('save_path>')

    for url in page:
       sum= download(url,save_path)
       if sum==None:
           break
       count=count-1
       print url,'页的图片数\t',sum, '\t剩余页数\t', count

