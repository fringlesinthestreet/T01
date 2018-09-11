from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    ip = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)


    def __init__(self, text, ip, date):
        self.text = text
        self.ip = ip
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
