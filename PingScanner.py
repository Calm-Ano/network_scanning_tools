# coding: utf-8

from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1
import ipaddress


def gen_iplist(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    netmask = ipaddress.ip_address(netmask)
    netaddr = ipaddress.ip_address(int(netmask) & int(ipv4))

    cidr = bin(int(netmask)).count('1')
    print(str(netaddr) + '/' + str(cidr))
    ip_network = ipaddress.ip_network(str(netaddr) + '/' + str(cidr))

    return ip_network.hosts()


def main():
    my_ip = input('Input this hosts IP addr :')
    netmask = input('Netmask :')

    ip_list = gen_iplist(my_ip, netmask)
    used_ip = list()

    for ip in ip_list:
        print('Trying to {}'.format(ip))
        pkt = IP(dst=str(ip), ttl=64)/ICMP()
        reply = sr1(pkt, timeout=3)

        if reply is not None:
            used_ip.append(ip)

    for ip in used_ip:
        print('{}\tis up'.format(ip))


if __name__ == '__main__':
    main()