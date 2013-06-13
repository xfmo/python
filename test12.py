#!/usr/lib/env python
#-*-coding:utf-8-*-
import urllib,urllib2,re

def get_url(url):
    req=urllib2.Request(url,headers={'User-Agent':'Magic Browser'})
    content=urllib2.urlopen(url).read()
    regx="""<a\shref="(http://.*?)"\stitle="(.*?)"\s.*?>(.*?)</a>"""
    regx2="""<a\shref="(http://.*?)".*?title="(.*?)".*?>(.*?)</a>"""
    img =re.compile(regx2)
    result=img.findall(content)
    for r in result:
        print r[0],r[1]
        # print result
if __name__=="__main__":
    get_url("http://www.youku.com")

