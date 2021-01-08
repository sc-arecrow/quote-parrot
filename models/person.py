from app import db

from models.quote import Quote


class Person(db.Document):
    name = db.StringField(required=True, unique=True)
    quotes = db.ListField(db.EmbeddedDocumentField(Quote))

    @staticmethod
    def make_person(name):
        return Person(name=name, quotes=[])