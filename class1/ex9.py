#!/usr/bin/env python

import re
from ciscoconfparse import CiscoConfParse

def main():

    cisco_file = 'cisco_ipsec.txt'
    
    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',childspec=r'pfs group2')
    print "\nCrypto Maps with PFS Group 2"

    for c_map in crypto_maps:
        #print c_map.text
        print "  {0}".format(c_map.text)
    print

if __name__ == "__main__":
    main()


