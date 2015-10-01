__author__ = '@abhinavbom a.k.a darkl0rd'

import sys
import os
import urllib2
from xml.dom import minidom
from urllib import quote

from lib.parse import *

# Base API URL
base_url = 'http://api.urlvoid.com/'

# API Key . Key can be obtained from api.urlvoid.com
api_key = ''+'/'

# plan identifier. change this value as per your plan in URLvoid. Free plans are designated by api1000 which is the
#default value here.

plan = 'api1000/'

#search for a host in URLvoid
detect = 'host/'

def urlvoid(url):
    c=0
    print "Conneting to URLVoid"
    while c < len(url):
        #print url[c]
        final_url = base_url+plan+api_key+detect+url[c]
        proxy = urllib2.ProxyHandler({'http': HTTP_PROXY, 'https': HTTPS_PROXY})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        req = urllib2.urlopen(final_url)
        resp = req.read()
        tree = minidom.parseString(resp)
        print tree
        obs_value = tree.getElementsByTagName('detections')
        for value in obs_value:
            print value.firstChild.nodeValue
        
        #for detections in tree.iter('detections'):
        #    print detections.attrib
        #print resp
        c+=1
