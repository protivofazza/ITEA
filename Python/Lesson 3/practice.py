from time import time
from functools import wraps


def decorator(number_of_calls):
    def actual_decorator(func_to_decorate):
        @wraps(func_to_decorate)
        def wrapper(arg_x, start_time):
            for i in range(number_of_calls):
                arg_x = func_to_decorate(arg_x)
                print(f'Function {func_to_decorate.__name__} has taken {time()-start_time}s to iterate this time')
                start_time = time()
            return arg_x

        return wrapper

    return actual_decorator


@decorator(5)
def square(x):
    return x ** 2


print(square(5, time()))
# print(square.__name__)
