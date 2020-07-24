from flask import Flask
from flask_restful import Api
from resources.ride import Ride, RideList
from db import db

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'erin1234'


@app.before_first_request
def create_table():
    db.create_all()

@app.route('inspect/http', methods=['GET'])
def respond():
    return Response({ “hub.challenge”:”7b601dcaee0c1371” }), 200

api.add_resource(Ride, '/ride/<string:name>')
api.add_resource(RideList, '/rides')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
