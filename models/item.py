import sqlite3
from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    complaint_details = db.Column(db.String(400))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, complaint_details, user_id):
        self.complaint_details = complaint_details
        self.user_id = user_id
    
    def json(self):
        return {"id":self.id, "user":self.user_id, "complaint_details": self.complaint_details}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #ItemModel.query.filter_by(name=name).first #ItemModel.query.filter_by(name=name, id=1)

    @classmethod
    def find_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
    
    def insert_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

