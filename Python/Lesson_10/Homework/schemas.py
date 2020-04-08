from marshmallow import Schema, fields, ValidationError, validate


class CategorySchema(Schema):
    id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=3))
    parent_category = fields.String()


class GoodsSchema(Schema):
    id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1))
    model = fields.String(required=True, validate=validate.Length(min=1))
    available = fields.Integer(required=True, validate=validate.Range(min=0, min_inclusive=True))
    category = fields.String(required=True)
    price = fields.Integer(required=True, validate=validate.Range(min=0, min_inclusive=True))
    seen_by = fields.Integer(default=0, validate=validate.Range(min=0, min_inclusive=True))
