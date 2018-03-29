#!/usr/bin/env python

from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('192.168.122.3','dilraj','dilraj')
device.open()

print ('Connection Established with 192.168.133.3')

device.load_merge_candidate(filename='acl_config_set.cfg')
	
diff = device.compare_config()
if (diff>0):
    print('New Configuration Found!! Adding below lines:')
	print(diff)
	device.commit_config()
else:
    print('Nothing new to Add in regards to ACL!')
    device.discard_config()

device.load_merge_candidate(filename='ospf_config_set.cfg')
	
diff = device.compare_config()
if (diff>0):
    print('New Configuration Found!! Adding below lines:')
	print(diff)
	device.commit_config()
else:
    print('Nothing new to Add in regards to OSPF!')
    device.discard_config()

device.close()