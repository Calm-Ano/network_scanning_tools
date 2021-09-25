# coding: utf-8

import socket
import sys


def main(host):
    ports = range(1, 10000)

    for port in ports:
        sock = socket.socket()
        ret = sock.connect_ex((host, port))

        print(port, end='\t')

        if ret == 0:
            print(str(port) + 'open')


if __name__ == '__main__':
    main(sys.argv[1])
