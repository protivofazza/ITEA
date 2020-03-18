class MyStruct:

    def __init__(self, *args):
        self._container = [*args]

    def __getitem__(self, item):
        return self._container[item]

    def __setitem__(self, key, value):
        self._container[key] = value


a = MyStruct(1, 2, 3, 4, 5)

for i in a:
    print(i)