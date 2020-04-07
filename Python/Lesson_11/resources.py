from flask_restful import Resource
from models import Passenger, Trip, Bus
from schemas import (PassengerSchema,
                     TripSchema,
                     TripPostSchema,
                     BusSchema,
                     ValidationError)
from flask import request


class TripResource(Resource):

    def get(self):
        trips = Trip.objects
        return TripSchema().dump(trips, many=True)

    def post(self):
        try:
            trip = TripPostSchema().dump(request.get_json())
        except ValidationError as err:
            return str(err)
        trip = Trip.objects.create(**trip)
        return TripSchema().dump(trip)

    def put(self):
        pass

    def delete(self):
        pass


class PassengerResource(Resource):

    def get(self):
        passengers = Passenger.objects
        print(passengers)
        return PassengerSchema().dump(passengers, many=True)

    def post(self):
        try:
            data = PassengerSchema().load(request.get_json())
        except ValidationError as err:
            return str(err)
        passenger = Passenger.objects.create(**data)
        return PassengerSchema().dump(passenger)


class BusResource(Resource):
    def get(self):
        buses = Bus.objects
        return BusSchema(only=('id',)).dump(buses, many=True)

    def post(self):
        try:
            data = BusSchema().load(request.get_json())
        except ValidationError as err:
            return str(err)
        bus = Bus.objects.create(**data)
        return BusSchema().dump(bus)