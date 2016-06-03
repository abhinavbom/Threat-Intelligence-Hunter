__author__ = '@abhinavbom a.k.a darkl0rd'

import urllib2
import urlparse
import re
import os
import time
from lib.feeds import *
from lib.parse import *

def gather():
    if not os.path.exists('intel'):
        os.mkdir('intel')
    os.chdir('.\\intel')
    #print os.getcwd()
    print "Starting feed update process"
    counter = 0
    ioc_list = []
    timestr = time.strftime("%Y%m%d-%H%M%S")
    for source in OSINT_IP.iteritems():
        if not os.path.exists(str(source[0])):
            os.mkdir(str(source[0]))
        print os.getcwd()
        os.chdir(str(source[0]))
        print source[0]
        name = str(source[0]) +"_" + timestr + ".txt"
        print name
        print "Building database"
        file = open(name, 'a+')
        r = requests.get(str(source[1]),
                        headers=create_basic_headers(),
                        proxies={'http': HTTP_PROXY, 'https': HTTPS_PROXY})
        for line in r:
            if line.startswith("/") or line.startswith('\n') or line.startswith("#"):
                pass
            else:
                file.write(line+'\n')
        os.chdir("..")
