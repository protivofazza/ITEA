def func_a(a):
    def func_b(b):
        def func_c(c):
            print(a, b, c)

        return func_c

    return func_b


result = func_a(10)(20)(30)
print(result)


def decorator(write_to_file):
    def actual_decorator(func_to_decorate):
        def wrapper(*args):
            r = func_to_decorate(*args)
            file = open('logs.txt', 'w')
            if write_to_file:
                file.write(r)
            else:
                print(r)
            file.close()
            return r

        return wrapper
    return actual_decorator


@decorator(True)
def func_test(string_to_test, second_string_to_test):
    return string_to_test + second_string_to_test


result = func_test("123", "23")


# result = func_test("123", "23")
# ==
# res = decorator(True)(func_test)("123", "23")