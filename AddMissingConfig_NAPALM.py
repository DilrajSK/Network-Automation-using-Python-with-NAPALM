#!/usr/bin/env python

from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver ('192.168.122.3','dilraj','dilraj')
device.open()

print ('Accessing 192.168.133.3...')
device.load_merge_candidate(filename='new_config_set')

diff = device.compare_config()

if len(diff)>0:
    print ('Writing new config to the device. Below statements will be added:')
	print (diff)
	device.commit_config()
else:
    print ('No new Configuraiton to add')
	device.discard_config()

device.close()