def method(self):
    print('Hi')


MyClass = type(
    'MyClass',
    (),
    {
        'the_first_attr': 1,
        'get_smth': method
    }
)


obj_of_my_cl = MyClass()
#print(obj_of_my_cl.get_smth())


class UsefulMethods:

    def make_class_feel_good(self):
        print('Feeling good')


class MyMeta(type):

    def __new__(mcls, name, bases, attributes):
        bases += (UsefulMethods, object)
        print(name, bases, attributes)
        return super().__new__(mcls, name, bases, attributes)


class Point(metaclass=MyMeta):

    name = 'PointClass'

    def __init__(self, x):
        self._x = x


a = Point(1)