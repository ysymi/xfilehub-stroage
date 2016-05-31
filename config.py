import os

DEBUG = True
GET_IP_CMD = 'ifconfig| grep 192.168 | awk \'{print $2}\''
HOST = os.popen(GET_IP_CMD).read().strip() or 'localhost'
PORT = int(os.environ['PORT'])
ALL_PORTS = list(range(8000, 8010))

ROOT = os.path.dirname(__file__)
ROOT = os.path.join(ROOT, 'storages', 'storage#%s' % PORT)  # collect all storage dir
STORAGE_DIR = os.path.join(ROOT, 'chunks')
CHUNK_NOTE_PATH = os.path.join(ROOT, 'chunks.note')

CHUNK_NAME_FORMAT = '{filename}.chunk{seq:0>3}'
LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'
APP_INFO = {'host': HOST, 'port': PORT}

BUFFER_SIZE = 1024 * 1024
