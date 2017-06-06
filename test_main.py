# encoding: utf-8
import urllib2
import urllib
import ssl
import re
from lxml import etree
from urllib import quote
from urllib import unquote
import random
from random import Random

def search(query,num):
	query = quote(query)
	#filename = savefile
	httpHandler = urllib2.HTTPHandler(debuglevel=0)
	httpsHandler = urllib2.HTTPSHandler(debuglevel=0)
	proxy=urllib2.ProxyHandler({'http': 'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'})
	opener = urllib2.build_opener(httpHandler,httpsHandler)
	#opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)

	ssl._create_default_https_context = ssl._create_unverified_context
	#header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
	count = 0
	for i in range(0,int(num)):
		gurl = getgoogleurl()
		l = random.randint(0,len(gurl)-1)
		gurl = gurl[l]
		#print gurl
		searchurl=gurl+"search?q="+ query +"&num=100&start="+str(i)+"00&lr=&cr=countryTW&newwindow=1&tbs=ctr:countryTW&btnG=Search&safe=active&gbv=1"
		#searchurl = "https://www.google.ca/search?q=filetype:action&num=100&lr=&cr=countryTW&newwindow=1&tbs=ctr:countryTW&btnG=Search&safe=active&gbv=1&filter=0"
		print searchurl
		req = urllib2.Request(searchurl)
		req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0")
		req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
		req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
		response = urllib2.urlopen(req)
		html = response.read()
		#print html;exit()
		selector = etree.HTML(html)
		x = geturls(selector)
		if x == 0:break
		#print x;exit()
		count = count + x
		response.close()
	print "本次抓取了"+str(count) + "条链接"

def geturls(selector):
	l=len(selector.xpath("//div[@class='g']/h3/a/@href"))
	if l == 0:return l
	for i in range(1,l+1):
		url = selector.xpath("substring-before(substring-after(//div[@class='g']["+str(i)+"]/h3/a/@href,'url?q='),'&sa=')")
		url = unquote(url)
		print url
		f = './urlout_numaction.txt'
		with open(f,'a+') as f:
			f.write(url+'\n')
		f.close()
	return l
def getgoogleurl():
	file = open('okgoogleurl.txt')
	lines = file.readlines()
	aa=[]
	for line in lines:
		temp = line.replace('\n','')
		aa.append(temp)
	return aa

'''
生成随机字符去搜索
'''
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

if __name__ == '__main__':
        for i in range(10):
                search(random_str(2)+' filetype:action','10')
