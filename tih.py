#local imports
from bin.feeds import *
from bin.parse import *

#stdlib imports
import argparse
import os
import sys

banner = ''' Threat Intelligence Hunter framework Begins now '''

print banner

def main():
    print "Intel test"
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-ip", type=str,  help="Enter the IP address to search through the list of feeds")

    args = parser.parse_args()
    if args.ip:
        ip_ioc = parse(args.ip)
        print ip_ioc

if __name__ == '__main__':
    main()

