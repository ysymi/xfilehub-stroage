import socket
from threading import Thread

import pexpect

ips = []


def ping(ip):
    cmd = pexpect.spawn('ping -c 1 %s' % ip)
    check = cmd.expect([pexpect.TIMEOUT, '0% packet loss'], 2)

    if check == 1:
        print(ip)
        ips.append(ip)


def get_ips():
    for i in range(100, 110):
        ip = '192.168.1.%s' % i
        t = Thread(target=ping, args=(ip,))
        t.start()
        t.join()
    return ips


print(get_ips())

