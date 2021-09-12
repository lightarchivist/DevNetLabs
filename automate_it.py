#!/usr/bin/env python

import logging
import netmiko

from __future__ import print_function, unicode_literals

# Netmiko is the same as ConnectHandler
from netmiko import ConnectHandler, redispatch
from getpass import getpass

#sends logs to test.log for troubleshooting purposes
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

#open file with list of devices
hostFile = open ('list-of-devices.txt','r')
hostList = hostFile.readlines()
hostFile.close()

#Password of the oparator that is making a change
mypass = getpass()

#new password for new local user
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
 output = net_connect.send_config_from_file("change-add-user.txt")
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
