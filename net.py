from threading import Thread

import pexpect

ips = []


def is_alive(ip):
    cmd = pexpect.spawn('ping -c 1 %s' % ip)
    check = cmd.expect([pexpect.TIMEOUT, '0% packet loss'])
    if check == 1:
        ips.append(ip)
    return check == 1


def get_ips():
    for i in range(100, 110):
        ip = '192.168.1.%s' % i
        t = Thread(target=is_alive, args=(ip,))
        t.start()
        t.join(0.1)
    return ips


print(get_ips())
