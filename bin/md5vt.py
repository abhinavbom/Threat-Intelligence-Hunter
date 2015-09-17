#stdlib imports

import json
import argparse
import sys
import requests

#local imports

from bin.parse import *

    
def getReport(md5):
    #Add your public API key before starting.
    api = '100e582a15884a9c5cc37e298766065695e551fb1fc88ee05eadc85eacc3b61e'
    if api == '':
        print "No API key provided. Please add your VirusTotal public API key to /bin/md5vt.py"
        sys.exit(1)
    base = 'https://www.virustotal.com/vtapi/v2/'
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
