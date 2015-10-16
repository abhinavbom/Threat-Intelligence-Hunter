__author__ = '@abhinavbom a.k.a Darkl0rd'

#local import
from lib.feeds import *

#stdlib import
import sys
import requests

# for traffic inspection from eclipse only
DEBUG=False

# Proxy Support. Added local proxy for debugging purpose.
if DEBUG:
    HTTP_PROXY = '127.0.0.1:80'
    HTTPS_PROXY = '127.0.0.1:443'
# Add your own proxy server to pass traffic through it
else:
    HTTP_PROXY = ''  # Enter your proxy address
    HTTPS_PROXY = HTTP_PROXY    #enter HTTPS proxy address(remove the assigned HTTPS_PROXY variable)

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'

#Creating basic HTTP headers to avoid traffic being dropped by filters.
def create_basic_headers():
    headers = {}
    headers['User-Agent'] = USER_AGENT
    headers['Accept-Language'] = 'en-US,en;q=0.5'
    headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    return headers
# parse function calls feeds.sources and traverses each of them to look for the input vector.

def url_param():
    params={}
    return params

def connect(url,params):
    print "Connecting with", url
    try:
        r = requests.get(url,
                        headers = create_basic_headers(),
                        proxies = {'http': HTTP_PROXY, 'https': HTTPS_PROXY},
                        params=url_param())
        return r
    except Exception as exc:
        sys.stdout.write('[!] Could not connect to: %s\n' % url)
#        sys.stdout.write('Exception: %s' % exc)

def parse_ip(ip):
    counter = 0
    ioc_list = []
    for filename, source in OSINT_IP.iteritems():
        c = connect(source,params=url_param())
        for line in c:
            if line.startswith("/") or line.startswith('\n') or line.startswith("#"):
                pass
            else:
                counter += 1
                d = 0
                while d < len(ip):
                    if ip[d] in line:
                        print ip[d], source

                    d +=1

    print "Total scanned indicators", counter


def parse_ipList(list):
    counter = 0
    ioc_list = []
    for filename, source in OSINT_ip.iteritems():
        c = connect(source)
        list = open("items.txt", "r")
        for items in list.readlines():
            for line in c:
                if line.startswith("/") or line.startswith('\n') or line.startswith("#"):
                    pass
                else:
                    counter += 1
                    if items in line:
                        print items, filename

    print "Total scanned indicators", counter
