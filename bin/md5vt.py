#stdlib imports

import json
import argparse
import sys
import requests

#local imports

from bin.parse import *

    
def getReport(md5):
    api = ''
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
    print r.json()
    if r.status_code == 0:
        print md5 + " -- Not Found in VT"
        return 0
