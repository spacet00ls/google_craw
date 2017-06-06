import random
#print random.randint(0,52)
import re

file = open('./urlout_numaction.txt','r')
lines = file.readlines()
urls=[]
for line in lines:
	temp = line.replace('\n','')
	#print len(temp)
	if len(temp)==0: break
	urls.append(temp)
	#print temp
	
	#print ss
	#if ss != None:
	#	print ss.group(0)
file.close()
	
#urls.append(temp)

new_urls=[]
for url in urls:
	url1 = re.match(r'http[s]{0,1}://(.*)\.[a-zA-Z]+/{0,1}(.?){0}',url)
	url2 = re.
	if url not in new_urls:
		outFile = open('./gproxy.txt','a+')
		outFile.write(url + '\n')
		outFile.close()
		new_urls.append(url)
#print new_urls
'''