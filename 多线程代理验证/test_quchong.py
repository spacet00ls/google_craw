import random
print random.randint(0,52)

file = open('./outproxy.txt','r')
lines = file.readlines()
urls=[]
for line in lines:
	temp = line.replace('\n','')
	urls.append(temp)
new_urls=[]
for url in urls:
	if url not in new_urls:
		outFile = open('./gproxy.txt','a+')
		outFile.write(url + '\n')
		outFile.close()
		new_urls.append(url)
#print new_urls


