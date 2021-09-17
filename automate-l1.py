#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# this script adds new local user for all devices included ipListOfNodes file 

# Netmiko is the same as ConnectHandler
from netmiko import ConnectHandler, redispatch
from netmiko import Netmiko
from getpass import getpass

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

hostFile = open ('ipListOfNodes','r')
hostList = hostFile.readlines()
hostFile.close()

mypass = getpass()  // operators/admin password 
adpass = getpass()  // password for a new local user

# adjust aaa settings and save
for device in hostList:
 huawei = {
        "host": device,
        "username": "username",
        "password": mypass,
        "device_type": "huawei",
		}
 net_connect = Netmiko(**huawei)
 output = net_connect.send_config_from_file("change_file.txt") // change file contain new local user configuration
 print(output)
 net_connect.disconnect()

# verify admin user and pwd
for device in hostList:
 huawei = {
        "host": device,
        "username": "admin",
        "password": adpass,
        "device_type": "huawei",
                }
 net_connect = Netmiko(**huawei)
 output = net_connect.send_config_from_file("verification")
 print(output)
 net_connect.disconnect()