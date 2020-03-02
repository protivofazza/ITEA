from time import time
from functools import wraps


def decorator(number_of_calls):
    def actual_decorator(func_to_decorate):
        @wraps(func_to_decorate)
        def wrapper(arg_x, *args, **kwargs):
            if args:
                print("All arguments starting from the 2nd one are ignored")
            if kwargs:
                print("All key arguments are ignored")
            result = [arg_x]
            for i in range(number_of_calls):
                start_time = time()
                result.append(func_to_decorate(result[-1]))
                print(f'Function {func_to_decorate.__name__} has taken {time()-start_time}s to iterate this time')
            return result

        return wrapper

    return actual_decorator


@decorator(5)
def square(x):
    return x ** 2


print(square(5, 6))
# print(square.__name__)
