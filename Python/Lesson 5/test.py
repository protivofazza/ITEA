def s(a1, b1):
    print(a1+b1)


class A:

    def __new__(cls, *args, **kwargs):
        s(args[0], args[1])
        print("HELLO")
        return super().__new__(cls)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


a = A(2,3)
print(a.name, a.surname)