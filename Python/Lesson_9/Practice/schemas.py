from marshmallow import Schema, ValidationError, fields, validate


class SubjectSchema(Schema):
    _id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=128))


class GradeSchema(Schema):
    _id = fields.String(required=True, dump_only=True)
    subject = fields.String(required=True)
    grade = fields.Int(required=True, validate=validate.Range(min=0, max=100))


class CuratorSchema(Schema):
    _id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=128))
    surname = fields.String(required=True, validate=validate.Length(min=1, max=128))


class DepartmentSchema(Schema):
    _id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=128))


class StudentSchema(Schema):
    _id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=128))
    surname = fields.String(required=True, validate=validate.Length(min=1, max=128))
    grades = fields.List(fields.String())
    curator = fields.String(required=True)
    department = fields.String(required=True)
