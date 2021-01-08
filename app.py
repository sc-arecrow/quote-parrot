from flask import Flask
app = Flask(__name__)

from controller import *

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)