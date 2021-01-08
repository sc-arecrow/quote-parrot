from app import db
import datetime


class Quote(db.EmbeddedDocument):
    text = db.StringField(required=True)
    date = db.DateTimeField(required=True)

    @staticmethod
    def make_quote(text):
        return Quote(text=text, date=datetime.datetime.now())