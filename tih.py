__author__ = '@abhinavbom a.k.a Darkl0rd'

#local imports
from lib.parse import *
from api.vt import *
from api.urlvoid import *
from lib.updatefeed import gather

#stdlib imports
import argparse

banner = ''' Threat Intelligence Hunter framework Begins now '''

print banner

def main():
    print "Intel test"
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-ip', type=str, nargs='+', help="Search for a single IP through OSINT threat feeds")
    
    parser.add_argument('-list', type=str, nargs='?', help="Search for a list of IP vectors. Accepted formats is .txt")
    
    parser.add_argument('-md5', type=str, nargs='+', help="Search for a single of space separated multiple MD5s. "
                                                          "This search is performed on Virustotal hence only 4 searches "
                                                          "per minute is allowed. Please add your public key to bin/vt.py")

    parser.add_argument('-url', type=str, nargs='+', help="Search for a single of space separated multiple urls. "
                                                          "This search is performed on Virustotal hence only 4 searches "
                                                          "per minute is allowed. Please add your public key to bin/vt.py")

    parser.add_argument('-repo', type=str, nargs='?', help="Search for the reputation of a list of URLs. The script"
                                                           "accepts a txt file containing list of domains and searches it"
                                                           "against popular reputation tools like URLVoid, Bluecoat etc.")
    parser.add_argument('-update', action='store_true', help='Update the local storage of feeds data.')
    args = parser.parse_args()
    if args.ip:
        if len(args.ip) > 4:
            print "Too many argument values specified. Maximum arguments per minute is 4."
            sys.exit(1)
        parse_ip(args.ip)
        vt_ip(args.ip)
    if args.list:
        parse_ipList(list)
    if args.md5:
        if len(args.md5) > 4:
            print "Too many argument values specified. Maximum arguments per minute is 4."
            sys.exit(1)
        vt_md5(args.md5)
    if args.url:
        if len(args.url) > 4:
            print "Too many argument values specified. Maximum arguments per minute is 4."
            sys.exit(1)
        vt_url(args.url)
    if args.repo:
        urlvoid(args.repo)
    if args.update:
        print "updating"
        gather()

if __name__ == '__main__':
    main()
