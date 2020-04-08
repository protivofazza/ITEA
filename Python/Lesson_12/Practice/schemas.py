from marshmallow import Schema, ValidationError, validate, fields


class PersonSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    surname = fields.String(required=True, validate=validate.Length(min=1, max=50))
    phone_number = fields.String(required=True, validate=validate.Length(min=13, max=13))
    email = fields.Email(required=True)
    address = fields.String(required=True, validate=validate.Length(min=1, max=500))
    comments = fields.String(required=True, validate=validate.Length(min=1, max=1000))
