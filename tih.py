__author__ = '@abhinavbom a.k.a Darkl0rd'

#local imports
from bin.parse import *

#stdlib imports
import argparse

banner = ''' Threat Intelligence Hunter framework Begins now '''

print banner

def main():
    print "Intel test"
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-ip', type=str, nargs='+', help="Search for a single IP through OSINT threat feeds")
    parser.add_argument('-list', type=str, nargs='?', help="Search for a list of IP vectors. Accepted formats is .txt")
    args = parser.parse_args()
    if args.ip:
        ip_ioc = parse_ip(args.ip)
        print ip_ioc

if __name__ == '__main__':
    main()
