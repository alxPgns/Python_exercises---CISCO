#!/usr/bin/env python
from socket import inet_ntoa
from struct import pack
import sys
import ipaddress

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def validate_submask(s):
    i = 0
    for x in s:
        if not x == '/' and i == 0:
            print("You must enter '/' before digits")
            return False
        elif x == '/':
            i = 1
            continue
        else:
            if not x.isdigit():
                print("Subnet mask must be an integer between 0 and 32")
                return False

    y = s.split("/")
    y1 = int(y[1])
    if not y1 < 0 and y1 > 32:
        return False

    return True


# binary to decimal
def calcDottedNetmask(mask):
    bits = 0
    for i in range(32-mask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))


# if IP address is valid, flag becomes 1. If not used, after one failed attempt of sub mask, ip would be requested again
flag = 0
while True:
    if flag == 0:
        IP_address = input("Enter IP address:")
        val1 = validate_ip(IP_address)
        if not val1:
            print("Invalid IP address format")
            continue
    flag = 1
    Subnet_mask = input("Enter subnet mask in decimal format:")
    val2 = validate_submask(Subnet_mask)
    if not val2:
        print("Subnet mask is invalid")
        continue

    ip = '.'.join([bin(int(x) + 256)[3:] for x in IP_address.split('.')])  # convert decimal (IP_address) -> binary (ip)
    s = Subnet_mask.split('/') # remove '/' special character from prefix
    mask = calcDottedNetmask(int(s[1])) # convert prefix (/24) to decimal dotted submask (e.g 255.255.255.0)
    mask_bin = '.'.join([bin(int(x) + 256)[3:] for x in mask.split('.')])  # decimal -> binary for and bitwise operation
    tmp = [ord(a) & (ord(b)) for a,b in zip(ip,mask_bin)]  # and between IP address and subnet mask, to find network IP
    network_address_list = [chr(i) for i in tmp]  # convert ASCII format to binary 48->0, 49->1
    network_address = ''.join(network_address_list)  # convert list -> string (network address, binary dotted format)

    a = IP_address.split('.')
    str1 = '\t\t'.join(str(e) for e in a)
    b = ip.split('.')
    str2 = ' '.join(str(e) for e in b)
    print("   ", str1)  # print ip address in decimal
    print(str2)        # print ip address in binary
    c = network_address.split('.')
    d = [int(i, 2) for i in c]
    str3 = '.'.join(str(e) for e in d)
    print("\n")
    print("network address is: {:s}{:s}".format(str3, Subnet_mask))

    # calculate and print broadcast address
    net = ipaddress.IPv4Network(IP_address + Subnet_mask, False)
    print("broadcast address is:", net.broadcast_address, Subnet_mask)
    break





