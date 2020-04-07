from flask import Flask
from flask_restful import Api
from resources import TripResource, PassengerResource, BusResource

app = Flask(__name__)
api = Api(app)

api.add_resource(TripResource, '/trips', '/trip/<id>')
api.add_resource(PassengerResource, '/passengers')
api.add_resource(BusResource, '/bus')

if __name__ == '__main__':
    app.run(debug=True)