# encoding: utf-8
import urllib2
import urllib
import ssl
import re
from lxml import etree
from urllib import quote
from urllib import unquote
import random

def search(query,num):
	query = quote(query)
	#filename = savefile
	httpHandler = urllib2.HTTPHandler(debuglevel=1)
	httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
	proxy=urllib2.ProxyHandler({'http': 'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'})
	opener = urllib2.build_opener(httpHandler,httpsHandler,proxy)
	#opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)

	ssl._create_default_https_context = ssl._create_unverified_context
	#header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
	count = 0
	for i in range(0,int(num)):
		#gurl = getgoogleurl()
		#l = random.randint(0,52)
		#gurl = gurl[l]
		#print gurl
		#searchurl=gurl+"search?q=hello&btnG=Search&safe=active&gbv=1"
		searchurl = "http://www.iyunv.com/thread-135490-1-1.html"
		print searchurl
		req = urllib2.Request(searchurl)
		req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0")
		req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
		req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
		response = urllib2.urlopen(req)
		html = response.read()
		#print html;exit()
		selector = etree.HTML(html)
		#print selector;exit()
		x = geturls(selector)
		count = count + x
		#print count
		#print "hehe"
		print "本次" + str(count) + "条链接"
		response.close()

def geturls(selector):
	aa = selector.xpath("//div[@class='t_fsz']/table/tr/td/a/@href")
	l = len(aa)
	for i in range(0,l):
		url = aa[i]
		url = unquote(url)
		print url
		f = './ggproxy.txt'
		with open(f,'a+') as f:
			f.write(url+'\n')
		f.close()
	return l

if __name__ == '__main__':
	search('filetype:action','1')