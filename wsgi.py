from flask import Flask
from conf import *

__author__ = 'an'

app = Flask(__name__)

if __name__ == '__main__':
    from view import *

    app.run(HOST, PORT, DEBUG)
