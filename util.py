import hashlib
import logging
import socket
from threading import Thread

import pexpect

from config import HOST, PORT, LOGGING_FORMAT


def calc_md5(data):
    if isinstance(data, (str, bytes)):
        m = hashlib.md5()
        m.update(data)
        return m.hexdigest()
    else:
        return ''


def ip_is_active(ip):
    global active_ips

    cmd = pexpect.spawn('ping -c 1 %s' % ip)
    check = cmd.expect([pexpect.TIMEOUT, '0% packet loss'], 0.5)
    if check == 1:
        active_ips.append(ip)
    return check == 1


def port_is_used(port, host='localhost'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
        return True  # port is used
    except Exception:
        return False


active_ips = []


def get_active_ips():
    global active_ips
    active_ips = []
    for i in range(100, 110):
        ip = '192.168.1.%s' % i
        t = Thread(target=ip_is_active, args=(ip,))
        t.start()
        t.join(0.1)
    return active_ips


def log_init():
    logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def log(msg):
    logging.info('%s:%s - %s' % (HOST, PORT, msg))
