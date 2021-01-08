from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'quote_parrot',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

from controller import *

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
