#!/usr/bin/env python

#Create a list and write it out to yaml and json

import yaml
import json

def main():
    
    yaml_file = "ex6_test.yml"
    json_file = "ex6_test.json"

    my_dict = {
        'ip_addr': '10.1.1.1',
        'platform': 'cisco_ios',
        'vendor': 'cisco',
        'model': '880'
    }

    my_list = [
        'string1',
        100,
        my_dict,
        'string2'
    ]

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list,default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(my_list, f)

if __name__ == "__main__":
    main()
            
