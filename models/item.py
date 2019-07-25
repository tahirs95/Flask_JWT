import sqlite3
from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    complaint_details = db.Column(db.String(400))

    def __init__(self, complaint_details):
        self.complaint_details = complaint_details
    
    def json(self):
        return {"id":self.id, "complaint_details": self.complaint_details}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #ItemModel.query.filter_by(name=name).first #ItemModel.query.filter_by(name=name, id=1)

    def insert_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

