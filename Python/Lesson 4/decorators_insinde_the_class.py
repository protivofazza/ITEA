class A:
    class Decorators:

        @staticmethod
        def decorator(func):
            def wrapper(*args):
                print(args)
                print(func)
                func(*args)

            return wrapper

    @Decorators.decorator
    def do_smth(self, arg1, arg2):
        pass


a = A()
a.do_smth(1, 2)
