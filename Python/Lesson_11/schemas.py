from marshmallow import (Schema,
                         fields,
                         ValidationError,
                         validates,
                         validate)


class BusSchema(Schema):
    id = fields.String(dump_only=True)
    model_ = fields.String(validate=validate.NoneOf(['Sprinter']))
    seats = fields.Int(validate=validate.Range(min=4, max=100))

    #@validates('model_')
    #def validate_model(self, value):
    #    if value == "Sprinter":
    #    raise ValidationError('Value cannot be "Sprinter"')


class TripSchema(Schema):
    id = fields.String(dump_only=True)
    destination = fields.String()
    bus = fields.Nested(BusSchema, dump_only=True)


class TripPostSchema(TripSchema):
    bus = fields.String()


class PassengerSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)
    trip = fields.String(dump_only=True)  # like read-only


