#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib2
import urllib
import re,os
#form download import download
#http://pp.163.com/poki/pp/7816141.html

def test(url):
    req=urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage=urllib2.urlopen(req)
    html_line=webpage.readline()
    while html_line:
        if html_line.find('data-lazyload-src'):
            print html_line
        html_line=webpage.readline()
    #soup=BeautifulSoup(webpage.read())
#callback
def urlcallback(a,b,c):
    print "callback"
    prec=100.0*a*b/c
    if 100<prec:
        prec=100
    print "%.2f%%"%(prec,)

def get_url(url):
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
               urllib.urlretrieve(href,os.path.join('/home/xfmo/my_python_test/girl/',image_name))
              # print image_name+" ok"
               img_sum+=1
            except:
                print "cannot download this image :"+href
        else:
            print  href+"is not a right url"
    return img_sum
   # print "success :",img_sum
def get_page(url):
    page_url=[]
    req=urllib2.Request(url,headers={'User-Agent':"Magic Browser"})
    webpage=urllib2.urlopen(req).read()
    href_com=re.compile("""<a href="(.*?)" .*?>.*?</a> """)
    href_list=href_com.findall(webpage)
    for href in href_list:
     if href.find("""http://""")==0 and href.endswith('.html'):
        # print href
         page_url.append(href)
    return page_url
if __name__=="__main__":
   # test(url_header)
   url=['http://pp.163.com/poki/pp/9806131.html','http://pp.163.com/poki/pp/7570037.html']
   #for url_header in url:
    # get_url(url_header)
   #page= get_page('http://poki.pp.163.com/')
   page=get_page('http://oldrabbit.pp.163.com/')
   print page
   count= len(page)
   for url in page:
       sum= get_url(url)
       print url,'页的图片数',sum
       count=count-1
       print '剩余页数', count

