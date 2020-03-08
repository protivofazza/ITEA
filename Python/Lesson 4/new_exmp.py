class Point:
    fields = ('id_', 'n ame', 'nickname')
    _instances = None

    def __new__(cls, *args, **kwargs):
        if cls._instances:
            raise Exception("It's a singletone type")
        else:
            cls._instances = super().__new__(cls)
            for field in cls.fields:
                setattr(cls._instances, field, 100)
                #print(getattr(cls._instances, 'id_'))
            return cls._instances

    def __init__(self, z):
        self._z = z


a = Point(1)

print(dir(a))
print(getattr(a, 'n ame'))
