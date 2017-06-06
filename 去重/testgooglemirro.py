# encoding: utf-8
import urllib2
import urllib
import ssl
import re
from lxml import etree
from urllib import quote
from urllib import unquote
import random
import re
import threading

httpHandler = urllib2.HTTPHandler(debuglevel=0)
httpsHandler = urllib2.HTTPSHandler(debuglevel=0)
proxy=urllib2.ProxyHandler({'http': 'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'})
opener = urllib2.build_opener(httpHandler,httpsHandler)
#opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

def search():
	#query = quote(query)
	#filename = savefile


	ssl._create_default_https_context = ssl._create_unverified_context
	#header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
	count = 0
	#for i in range(1):
	while True:
		lock.acquire()
		lines = file.readline().replace('\n','')
		gurl = lines
		#print gurl;exit()
		lock.release()
		#print gurl;break
		if len(gurl) == 0:break
		searchurl=gurl+"/search?q=test&num=0&lr=&cr=countryTW&newwindow=1&tbs=ctr:countryTW&btnG=Search&safe=active&gbv=1&filter=0"
		#searchurl = "https://www.google.ca/search?q=filetype:action&num=100&lr=&cr=countryTW&newwindow=1&tbs=ctr:countryTW&btnG=Search&safe=active&gbv=1&filter=0"
		#print searchurl
		
		req = urllib2.Request(searchurl)
		req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0")
		req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
		req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
		try:
			response = urllib2.urlopen(req)
			html = response.read()
			#print html;exit()
			response.close()
			#print html;exit()
			selector = etree.HTML(html)
			if (geturls(selector)):
				lock.acquire()
				outFile = open('okgoogleurl.txt','a+')
				outFile.write(gurl + '\n')
				print 'this ' + gurl + ' is ok.'
				outFile.close()
				lock.release()
			else:
				print 'this ' + gurl + ' is bad.'
		except Exception, e:
			print e
			print '\n'



def geturls(selector):
	ss = selector.xpath("//meta[2]/@content")
	#print ss;exit()
	gg = re.search(r'google',ss[0])
	if gg.group() != None:
		return True
	else:
		return False


lock = threading.Lock()
file = open('outproxy.txt','r')
all_thread = []
for i in range(20):
    t = threading.Thread(target=search)
    all_thread.append(t)
    t.start()
    
for t in all_thread:
    t.join()
file.close()
