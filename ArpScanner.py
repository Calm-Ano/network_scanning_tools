# coding: utf-8

from scapy.all import Ether
from scapy.all import ARP
from scapy.all import srp
import ipaddress
import uuid
import re


def main():
    my_ip = input('Input this IP address: ')
    netmask = input('Input this netmask: ')
    hwaddr = 'ff:ff:ff:ff:ff:ff'    # broad cast
    # hwaddr = ':'.join(re.split('(..)', format(uuid.getnode(), 'x'))[1::2])

    cidr = gen_cidr(my_ip, netmask)

    print('Scanning on: ' + cidr + '\n')

    pkt = Ether(dst=hwaddr)/ARP(op=1, pdst=cidr)
    ans, uans = srp(pkt, timeout=2)

    print('')
    for send, recv in ans:
        print(recv.sprintf('%ARP.psrc% is up'))


def gen_cidr(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    netmask = ipaddress.ip_address(netmask)
    netaddr = ipaddress.ip_address(int(ipv4) & int(netmask))
    netaddr = str(netaddr).split('/')[0]
    cidr = bin(int(netmask)).count('1')
    return str(netaddr) + '/' + str(cidr)


if __name__ == '__main__':
    main()