from flask import Flask
from conf import *

__author__ = 'an'

app = Flask(__name__)
from view import *
if __name__ == '__main__':
	app.run(HOST, PORT, DEBUG)