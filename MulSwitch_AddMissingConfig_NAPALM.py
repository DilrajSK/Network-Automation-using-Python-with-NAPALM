#!/usr/bin/env python

from napalm import get_network_driver

device_list=['192.168.122.2',
    '192.168.122.1'
	]

for ipaddress in device_list:
    print ('Accessing ' + str(ipaddress))
	driver = get_network_driver('ios')
	driver = get_network_driver('ios')
	device = driver(ipaddress,'dilraj','dilraj')
	device.open()
	
	device.load_merge_candidate(filename='config_set.cfg')
	
	diff = device.compare_config()
	if (diff>0):
	    print('New Configuration Found!! Adding below lines:')
		print(diff)
		device.commit_config()
	else:
	    print('Nothing new to Add!')
        device.discard_config()
    device.close()		