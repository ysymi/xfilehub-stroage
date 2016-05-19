from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    file_list = []  # block_index.get().keys()
    return render_template('index.html', file_list=file_list)


@app.route('/upload', methods=['POST'])
def upload():
    pass


@app.route('/download/<filename>')
def download(filename):
    pass


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
