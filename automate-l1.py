#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# this script adds new local user for all devices included ipListOfNodes file 

import logging

# Netmiko is the same as ConnectHandler
from netmiko import ConnectHandler, redispatch
from netmiko import Netmiko
from getpass import getpass

# logging for troubleshooting purposes
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

hostFile = open ('ipListOfNodes','r')
hostList = hostFile.readlines()
hostFile.close()


# admin password
mypass = getpass()

# new password for the new local user 
adpass = getpass() 

# adjust aaa settings and save
for device in hostList:
    huawei = {
        "host": device,
        "username": "username",
        "password": mypass,
        "device_type": "huawei",
		}
    net_connect = Netmiko(**huawei)
    output = net_connect.send_config_from_file("change_file.txt") 
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
