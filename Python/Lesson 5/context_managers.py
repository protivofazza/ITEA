class ContextManagerExample:

    def __init__(self, string):
        self._string = string

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(*args)
        self._string = self._string[::-1]
        print('Exit called')


with ContextManagerExample('qwe') as string:
    string._string = 123
    string._string = "123"

print(string._string)
# with open('zxc.py', 'w') as file:
#   file.write('qwe')