__author__ = '@abhinavbom a.k.a darkl0rd'

import urllib2
import re
import os
import time
from lib.feeds import *
from lib.parse import *

if not os.path.exists('intel'):
    os.mkdir('intel')



def gather():
    counter = 0
    ioc_list = []
    timestr = time.strftime("%Y%m%d-%H%M%S")
    for source in OSINT_IP.iteritems():
        name = source + timestr
        file = open(name, 'w')
        c = connect(source,params=url_param())
        for line in c:
            if line.startswith("/") or line.startswith('\n') or line.startswith("#"):
                pass
            else:
                file.write(line+'\n')






    
