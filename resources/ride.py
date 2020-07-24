from flask_restful import Resource
from models.ride import RideModel


class Ride(Resource):
    def get(self, name):
        ride = RideModel.find_by_name(name)
        if ride:
            return ride.json()
        return {'message': 'Ride not found'}, 404


class RideList(Resource):
    def get(self):
        return {'rides': [ride.json() for ride in RideModel.query.all()]}
