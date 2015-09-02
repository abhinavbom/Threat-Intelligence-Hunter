#local import
from bin.feeds import *

#stdlib import
import urllib2
import os
import sys


def parse(ip):
    counter = 0
    ioc_list = []
    #hdr = {'User-Agent':'Mozilla/5.0'}
    #req = urllib2.Request(url, headers=hdr)
    #site = urllib2.urlopen(req)
    for filename, source in OSINT.iteritems():
        hdr = {'User-Agent':'Mozilla/5.0'}
        req = urllib2.Request(source, headers=hdr)
        site = urllib2.urlopen(req)
        print "Checking %s " %filename
        for line in site:
            if line.startswith("/") or line.startswith('\n') or line.startswith("#"):
                pass
            else:
                if ip in line:

                    for list in ip:
                        if list in ioc_list:
                            pass
                    else:
                        ioc_list.append(ip)
                        print ioc_list , source
                        counter += 1