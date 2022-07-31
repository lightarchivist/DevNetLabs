"""simple scrypt to enable netconf and restconf on lab devices"""
from netmiko import ConnectHandler

with open("hosts.log", "r") as hosts:
    print(hosts.read())

with open("commands.log", "r") as commands:
    print(commands.read())

