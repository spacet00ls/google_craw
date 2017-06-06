#encoding: utf-8
import re

#导入urls
inFile = open('urlout_numaction.txt','r')
old_urls = inFile.readlines()
inFile.close()
outFiles = open('quchongurls2.txt','w')
aa= []  #临时存放域名
for url in old_urls:
	temp = re.search(r'http[s]{0,1}://[\.a-zA-Z0-9-]+\.[a-zA-Z0-9:-]+/',url)
	aa.append(temp.group())
#print aa;exit()

new_urls =[]
for url1 in aa:
	for url2 in old_urls:
		temp = re.search(r'http[s]{0,1}://[\.a-zA-Z0-9-]+\.[a-zA-Z0-9:-]+/',url2)
		if temp.group() not in new_urls:
			outFiles = open('quchongurls2.txt','a+')
			outFiles.write(url2)
			outFiles.close()
			new_urls.append(temp.group())
			#print url2;exit()
