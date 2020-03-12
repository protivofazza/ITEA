class FacebookAuth:

    def __init__(self, login, password):
        self._login = login
        self._password = password

    @classmethod
    def validate(cls, login, password):
        print(cls)

    def __call__(self, *args, **kwargs):
        print("Object has been called")


class API(FacebookAuth):
    pass


fb = FacebookAuth('123', 'qwe')

fb()

API.validate('123', 'qwe')


class Dec:

    def __init__(self, func):
        self.f = func

    def __call__(self):
        print(f"Wrapping function {self.f.__name__}")
        self.f()


@Dec
def test():
    print('hello')

test()