"""simple scrypt to enable netconf and restconf on lab devices"""
from netmiko import ConnectHandler
import ipaddress

def validate_ipadd(address):
    try:
        ip = ipaddress.ip_address(address)
        print = ("IP address is valid ".format(address, ip))
    except ValueError:
        print("IP address is not valid".format(address))


with open("hosts.log", "r") as hosts:
    print(hosts.read())

with open("commands.log", "r") as commands:
    print(commands.read())

