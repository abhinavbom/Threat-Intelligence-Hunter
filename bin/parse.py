#local import
from bin.feeds import *

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
    HTTP_PROXY = 'http://proxy.jpmchase.net:8443'             #Enter your proxy address
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


def parse_ip(ip):
    counter = 0
    ioc_list = []
    for filename, source in OSINT.iteritems():
        sessions = requests.Session()
        print "Connecting with", source
        try:
            r = sessions.get(source,
                            headers = create_basic_headers(),
                            proxies = {'http': HTTP_PROXY, 'https': HTTPS_PROXY})
        except:
            sys.stdout.write('[!] Could not connect to: %s\n' % source)
        for line in r:
            if line.startswith("/") or line.startswith('\n') or line.startswith("#"):
                pass
            else:
                counter += 1
                if ip in line:
                    for list in ip:
                        if list in ioc_list:
                            pass
                    else:
                        ioc_list.append(ip)


    # print "Matched IP", ioc_list, "under following source", source
    print "Total scanned indicators",counter
