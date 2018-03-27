#!/usr/bin/env python

import json
from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.122.1','dilraj','dilraj')
device.open()

output = device.get_facts()
print (json.dumps(output, indent=4))

output = device.get_interfaces()
print (json.dumps(output, sort_keys=True, indent=4))

output = device.get_interfaces_counters()
print (json.dumps(output, sort_keys=True,  indent=4))

device.close()