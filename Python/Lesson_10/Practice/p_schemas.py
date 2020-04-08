from marshmallow import Schema, fields, ValidationError, validate


class TagSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=2, max=30))


class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    surname = fields.String(required=True, validate=validate.Length(min=1, max=50))
    number_of_publications = fields.Integer(validate=validate.Range(min=0))


class PublicationSchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1, max=300))
    post = fields.String(required=True, validate=validate.Length(min=1, max=10000))
    date = fields.DateTime(required=True)
    author = fields.String(required=True)
    tags = fields.List(fields.String())
    seen_by = fields.Int(validate=validate.Range(min=0))
