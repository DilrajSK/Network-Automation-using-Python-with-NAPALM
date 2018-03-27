#!/usr/bin/env python

from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver ('192.168.122.3','dilraj','dilraj')
device.open()

print ('Connected to 192.168.122.3')
device.load_merge_candidate(filename='config_set.cfg')
print device.compare_config()
device.commit_config()
device.close()