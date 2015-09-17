#stdlib imports

import json
import argparse
import sys
import requests

#local imports

from bin.parse import *

#Add your public API key before starting.
api = ''
base = 'https://www.virustotal.com/vtapi/v2/'
if api == '':
    print "No API key provided. Please add your VirusTotal public API key to /bin/md5vt.py"
    sys.exit(1)

def vt_md5(md5):
    param = {'resource':md5,'apikey':api}
    url = base + "file/report"
    #data = urllib.urlencode(param)
    #result = urllib2.urlopen(url,data)
    print "Connecting to Virustotal"
    r = requests.get(url,
                    headers=create_basic_headers(),
                    proxies={'http': HTTP_PROXY, 'https': HTTPS_PROXY},
                    params=param)
    data = r.json()
    if data['response_code'] == 0:
        print md5 + " -- Not Found in VT"
        return 0
    #print r.json()
    print "\n\tResults for MD5: ",md5,"\n\n\tDetected by: ",data['positives'],'/',data['total'],'\n'


def vt_ip(ip):
    param = {'ip':ip,'apikey':api}
    url = base + "ip-address/report"
    #data = urllib.urlencode(param)
    #result = urllib2.urlopen(url,data)
    print "Connecting to Virustotal"
    r = requests.get(url,
                    headers=create_basic_headers(),
                    proxies={'http': HTTP_PROXY, 'https': HTTPS_PROXY},
                    params=param)
    data = r.json()
    if data['response_code'] == 0:
        print ip + "---Not found in VT"
        return 0
    elif data['response_code'] == -1:
        print "Invalid IP address"
        return 0
    #print data
    elif data['response_code'] == 1:
        #print data
        for each in data['detected_communicating_samples']:
            print "\n\tDetected: ",each['positives'],'/',each['total']
