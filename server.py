import logging

# import tornado.web
# import tornado.ioloop
#
# from handler.main import MainHandler
# from handler.upload import UploadHandler
# from handler.download import DownloadHandler
# from config import PORT
#
#
# def make_app():
#     settings = {
#         'gzip': True,
#         'debug': True,
#         'static_path': 'static/',
#         'template_path': 'template/'
#     }
#     return tornado.web.Application([
#         (r'/', MainHandler),
#         (r'/upload', UploadHandler),
#         (r'/download', DownloadHandler),
#     ], **settings)
#
#
# if __name__ == '__main__':
#     logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
#     app = make_app()
#     app.listen(PORT)
#     tornado.ioloop.IOLoop.current().start()
#

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
