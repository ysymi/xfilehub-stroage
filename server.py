import os

from flask import Flask, render_template, request, Response,redirect
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    # return redirect('http://www.baidu.com')
    file_list = ['漫谈敏捷测试工具实现.pdf0']  # block_index.get().keys()
    return render_template('index.html', file_list=file_list)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload():

    # return redirect('http://localhost:5000/upload/', code=307)

    name = request.form['name']
    seq = request.form['seq']
    md5 = request.form['md5']
    data = request.files['data']

    path = os.path.join(os.path.dirname(__file__), name + seq)
    data.save(path)

    return 'ok'

    chunk = (name, seq, data, md5)

    # todo : give to storage
    pass


@app.route('/download/<filename>')
def download(filename):
    def generate():
        for letters in "this is suppose to be a big csv file iterator or something":
            yield letters + '\n'

    path = os.path.join(os.path.dirname(__file__), filename)

    def get_file(filename):
        f = open(path, 'rb')
        cnt = 0
        print(filename)
        while True:
            buf = f.read(1024*1024)
            if not buf:
                break
            cnt += 1
            print(cnt)
            yield buf

    return Response(get_file(filename),
                    mimetype="application/octet-stream",
                    headers={"Content-Disposition":
                                 "attachment;filename=test.pdf"})


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
