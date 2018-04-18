# -*- coding: utf-8 -*-
#Crawler.py
import urllib
import urllib2
import itertools
import urlparse
import datetime
import cookielib
import time
import re

class Crawler:
    htmls=[]
    cookies=cookielib.CookieJar()
    def download(self,url,headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'},num_retries=2):
        print 'Downloading:',url.decode('utf-8'),'\n'
        request=urllib2.Request(url,headers=headers)
        try:
            html=urllib2.urlopen(request).read()
        except urllib2.URLError as e:
            print 'Download error:',e.reason,'\n'
            html=None
            if num_retries > 0:
                if hasattr(e,'code') and 500 <= e.code < 600:
                    return self.download(url,num_retries=num_retries-1)
        return html

    def crawl_sitemap(self,url,max_errors=5,delay=0):
        sitemap=self.download(url)
        links=re.findall('<loc>(.*?)</loc>',sitemap)
        mThrottle=Throttle(delay)
        for link in links:
            if delay > 0:
                mThrottle.wait(link)
            html=self.download(link)
            self.htmls.append(html)

    def link_crawler(self,seed_url,link_regex,max_depth=-1,delay=0):
        crawl_queue=[seed_url]
        seen={seed_url:0}
        mThrottle=Throttle(delay)
        while crawl_queue:
            url=crawl_queue.pop()
            depth=seen[url]
            if delay !=0:
                mThrottle.wait(url) 
            if depth != max_depth:
                html=self.download(url)
                if html is None:
                    continue 
                for link in self.get_links(html):
                    if re.match(link_regex,link):
                        link=urlparse.urljoin(seed_url,link)
                        if link not in seen:
                            seen[link]=depth+1
                            crawl_queue.append(link)

    def get_links(self,html):
        webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
        return webpage_regex.findall(html)

    def ID_crawler(self,url,user_agent='wswp',max_errors=5,delay=0):
        num_errors=0
        mThrottle=Throttle(delay)
        for page in itertools.count(1):
            if delay > 0:
                mThrottle.wait(url % page)
            html=self.download(url % page,user_agent)
            if html is None:
                num_errors +=1
                if num_errors==max_errors:
                    break
            else:
                num_errors=0
                self.htmls.append(html)
    def clear(self):
        del self.htmls[:]

    def dynamic_download(self,url,data={},type='POST',headers={'user_agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2717.400 QQBrowser/9.6.11133.400'}):
        print 'Downloading:',url
        data=urllib.urlencode(data)
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        if type=='POST':
            request=urllib2.Request(url=url,headers=headers,data=data)
        else:
            url=url+'?'+data
            request=urllib2.Request(url=url,headers=headers)
        html=opener.open(request).read()
        return html

class Throttle:
    def __init__(self,delay):
        self.delay=delay
        self.domains={}

    def wait(self,url):
        domain=urlparse.urlparse(url).netloc
        last_accessed=self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs=self.delay-(datetime.datetime.now()-last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain]=datetime.datetime.now()
