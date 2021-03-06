import os

from flask import Flask, request, Response, jsonify
from flask.ext.cors import CORS

from chunk import chunks
from config import STORAGE_DIR, BUFFER_SIZE, PORT, CHUNK_NAME_FORMAT, HOST
from util import log_init, log

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'OK, I am running at %s' % PORT


@app.route('/chunks')
def get_chunks():
    # data = chunks.get_all()
    return jsonify(chunks=chunks.get_all())


@app.route('/info')
def get_info():
    log('/info is called')
    return jsonify(host=HOST, port=PORT, name='%s:%s' % (HOST, PORT))


@app.route('/upload', methods=['POST'])
def upload():
    name = request.form['name']
    seq = request.form['seq']
    md5 = request.form['md5']
    data = request.files['data']
    chunk_name = CHUNK_NAME_FORMAT.format(filename=name, seq=seq)

    log('upload chunk: %s' % chunk_name)
    # data =
    # xmd5 = calc_md5(data.read())
    if md5 == md5:  # TODO: md5 or read ?


        log(data.tell())

        chunk_path = os.path.join(STORAGE_DIR, chunk_name)
        data.save(chunk_path)
        chunks.insert(chunk_name, md5)
        log('upload success chunk:%s md5:%s ori(%s)' % (chunk_name, md5, md5))
        return 'ok'  # TODO: check ok status
    else:
        log('upload failed chunk:%s md5:%s' % (chunk_name, md5))
        return 'error'  # TODO: error process


@app.route('/download/<chunk_name>')
def download(chunk_name):
    def gen_chunk():
        chunk_path = os.path.join(STORAGE_DIR, chunk_name)
        log(chunk_path)
        count = 0
        with open(chunk_path, 'rb') as f:

            while True:
                buf = f.read(BUFFER_SIZE)
                if not buf:
                    break
                count += 1
                log('count %s' % count)

                yield buf

    # from flask import send_file
    # chunk_path = os.path.join(STORAGE_DIR, chunk_name)
    # return send_file(chunk_path)

    # TODO: check response

    return Response(gen_chunk())


if __name__ == '__main__':
    log_init()

    app.run(host=HOST, port=PORT, debug=False)
