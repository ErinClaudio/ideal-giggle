import sqlite3
from db import db


class RideModel(db.Model):
    __tablename__ = 'rides'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    distance = db.Column(db.Float(precision=3))
    total_elevation_gain = db.Column(db.Float(precision=3))

    def __init__(self, name, distance, total_elevation_gain):
        self.name = name
        self.distance = distance
        self.total_elevation_gain = total_elevation_gain

    def json(self):
        return {'name': self.name, 'distance': self.distance, 'total_elevation_gain': self.total_elevation_gain}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name)
