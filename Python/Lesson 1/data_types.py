temperature = 20

result = "hot" if temperature > 20 else "cold"

# print([i for i in range(5)])

k = [1, 2]

""""
try:
    b = (1 + 3 + 4) / 4
except ZeroDivisionError as e:
    b = e
    print("Finally Block")
else:
    print("No exception occurred")
finally:
    pass
"""


# print(b)


def sum_func(arg1, arg2):
    return sum([arg1, arg2])


# print(result)

def func1(sum_f, arg1, arg2):
    return sum_f(arg1, arg2)


def test_sum(*args):
    return sum(args) / len(args)


values = [100, 100, 100]
