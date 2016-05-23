import json
import os

import util
from config import CHUNK_NOTE_PATH, STORAGE_DIR, HOST, PORT
from util import log


class Chunks(object):
    def __init__(self):
        self._chunks = []
        self.recovery()
        if not self._chunks:
            self.rebuild()
            self.save()

    def recovery(self):
        if not os.path.exists(CHUNK_NOTE_PATH):
            log('chunk note is not exist')
            return

        with open(CHUNK_NOTE_PATH, 'r') as f:
            self._chunks = json.loads(f.read())

    def rebuild(self):
        chunk_names = os.listdir(STORAGE_DIR)
        for chunk_name in chunk_names:
            path = os.path.join(STORAGE_DIR, chunk_name)
            md5 = util.calc_md5(open(path, 'rb'))
            self._chunks.append({
                'name': chunk_name,
                'md5': md5,
                'host': HOST,
                'port': PORT
            })
        self.save()

    def save(self):
        with open(CHUNK_NOTE_PATH, 'w') as f:
            f.write(json.dumps(self._chunks, indent=2))

    def insert(self, chunk_name, md5):
        self._chunks.append({
            'name': chunk_name,
            'md5': md5,
            'host': HOST,
            'port': PORT
        })
        self.save()

    def get_all(self):
        return self._chunks


chunks = Chunks()
