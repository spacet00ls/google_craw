#encoding=gbk
import httplib
import time
import urllib
import threading
 
inFile = open('gproxy.txt', 'r')

 
lock = threading.Lock()
 
def test():
    while True:
        lock.acquire()
        line = inFile.readline().replace('\n','')
        line = line.replace('http://','')
        line = line.replace('https://','')
        line = line.replace('/','')
        lock.release()
        if len(line) == 0: break
        #protocol, proxy = line.split('=')
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': ''}
        try:
            #print line
            conn = httplib.HTTPConnection(line,80)
            conn.request(method='GET', url='/', body='/', headers=headers )
            res = conn.getresponse()
            ret_headers = str( res.getheaders() ) 
            html_doc = res.read().decode('utf-8')
            ret_status = res.status
            #print html_doc.encode('gbk')
            if ret_status == 200:
                lock.acquire()
                print 'add url', line
                outFile = open('available.txt', 'a+')
                outFile.write(line + '\n')
                outFile.close()
                lock.release()
            else:
                print '.',
        except Exception, e:
            print e
 
all_thread = []
for i in range(50):
    t = threading.Thread(target=test)
    all_thread.append(t)
    t.start()
    
for t in all_thread:
    t.join()
 
inFile.close()
#outFile.close()
