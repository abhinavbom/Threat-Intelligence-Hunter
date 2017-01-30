#stdlib imports

#local imports

from lib.parse import *

#Add your public API key before starting.
api = 'd'
base = 'https://www.virustotal.com/vtapi/v2/'
if api == '':
    print "No API key provided. Please add your VirusTotal public API key to /bin/md5vt.py"
    sys.exit(1)

def vt_md5(md5):
    c=0
    url = base + "file/report"
    #data = urllib.urlencode(param)
    #result = urllib2.urlopen(url,data)
    print "Connecting to Virustotal"
    while c < len(md5):
        param = {'resource':md5[c],'apikey':api}
        r = requests.get(url,
                        headers=create_basic_headers(),
                        proxies={'http': HTTP_PROXY, 'https': HTTPS_PROXY},
                        params=param)
        data = r.json()
        #print data
        if data['response_code'] == 0:
            print "\n\tResults for MD5: ", data['resource'], " -- Not Found in VT"
            print data['verbose_msg']
            #print r.json()
        else:
            print "\n\tResults for MD5: ",data['resource'],"\n\n\tDetected by: ",data['positives'],'/',data['total'],'\n'
        c+=1


def vt_ip(ip):
    c=0
    url = base + "ip-address/report"
    #data = urllib.urlencode(param)
    #result = urllib2.urlopen(url,data)
    print "Connecting to Virustotal"
    while c < len(ip):
        print "looking for IP", ip[c]
        param = {'ip':ip[c],'apikey':api}
        r = requests.get(url,
                        headers=create_basic_headers(),
                        proxies={'http': HTTP_PROXY, 'https': HTTPS_PROXY},
                        params=param)
        data = r.json()
        #print data
        if data['response_code'] == 0:
            print ip + "---Not found in VT"
        elif data['response_code'] == -1:
            print "Invalid IP address"
        #print data
        elif data['response_code'] == 1:
            #print data
            if 'detected_communicating_samples' in data :
                for each in data['detected_communicating_samples']:
                    print "\n\tDetected: ",each['positives'],'/',each['total']
            else:
                print "\nIP is not found in VT, but here is some info\n"
                print "Owner: ",data['as_owner']
                print "Country: ", data['country']
        c+=1


def vt_url(url2search):
    c=0
    url = base + "url/report"
    #data = urllib.urlencode(param)
    #result = urllib2.urlopen(url,data)
    print "Connecting to Virustotal"
    while c < len(url2search):
        print "looking for URL", url2search[c]
        param = {'resource':url2search[c],'apikey':api}
        r = requests.get(url,
                        headers=create_basic_headers(),
                        proxies={'http': HTTP_PROXY, 'https': HTTPS_PROXY},
                        params=param)
        data = r.json()
        #print data
        if data['response_code'] == 0:
            print url2search + "---Not found in VT"
        elif data['response_code'] == -1:
            print "Invalid IP address"
        #print data
        elif data['response_code'] == 1:
            print "Scanned VT url: ", data['permalink']
            print "\n Detection ratio", data['positives'], "/", data['total']

        c+=1
