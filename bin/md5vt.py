import simplejson
import urllib
import urllib2
from bin.parse import *
import requests

def hashVT():
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    parameters = {"resource": "99017f6eebbac24f351415dd410d522d",
                  "apikey": "100e582a15884a9c5cc37e298766065695e551fb1fc88ee05eadc85eacc3b61e"}
    data = urllib.urlencode(parameters)
    req = connect(url)
    response = urllib2.urlopen(req, headers=create_basic_headers())
    json = response.read()
    print json
