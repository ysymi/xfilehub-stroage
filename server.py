import logging
import os

from flask import Flask, request, Response
from flask.ext.cors import CORS

from ch import hashring

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload():

    name = request.form['name']
    seq = request.form['seq']
    md5 = request.form['md5']
    data = request.files['data']

    path = os.path.join(os.path.dirname(__file__), name + seq)
    data.save(path)
    chunk = (name, seq, data, md5)
    logging.info(chunk)

    hashring

    return 'ok'


@app.route('/download/<filename>')
def download(filename):


    path = os.path.join(os.path.dirname(__file__), filename)

    def get_file(filename):
        f = open(path, 'rb')
        cnt = 0
        print(filename)
        while True:
            buf = f.read(1024 * 1024)
            if not buf:
                break
            cnt += 1
            print(cnt)
            yield buf

    return Response(get_file('分层自动化测试持续集成_-_倪生华.pdf0'),
                    mimetype="application/octet-stream",
                    headers={"Content-Disposition":
                                 "attachment;filename=test.pdf"})


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    app.run(host='localhost', port=9000, debug=True)
