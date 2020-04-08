import models as m
import schemas as s

MODELS = tuple([i for i in dir(m) if i != 'me' and not i.startswith('__')])
SCHEMAS = tuple([i for i in dir(s) if i != 'me' and not i.startswith('__')])


def read(model, **kwargs):
    if model.__name__ not in MODELS:
        raise AttributeError("model argument must be a ModelClass object")
    if not kwargs:
        return model.objects
    try:
        return model.objects.filter(**kwargs)
    except AttributeError as err:
        return str(err)


def create(model, schema, dict_: dict):
    if model.__name__ not in MODELS:
        raise AttributeError("model argument must be a ModelClass object")
    if schema.__name__ not in SCHEMAS:
        raise AttributeError("schema argument must be a ModelClass object")
    try:
        obj = schema().load(dict_)
    except s.ValidationError as err:
        return str(err)
    return model.objects.create(**obj).save()


def update(model, schema, obj):
    if model.__name__ not in MODELS:
        raise AttributeError("model argument must be a ModelClass object")
    if schema.__name__ not in SCHEMAS:
        raise AttributeError("schema argument must be a ModelClass object")
    if not isinstance(obj, model):
        raise AttributeError("obj must be an instance of modelclass")
    try:
        ok = schema().dump(obj)
    except s.ValidationError as err:
        return str(err)
    return obj.save()
