class List:

    def __init__(self, *args):
        self._list = [*args]
        self._length = len(args)

    def append(self, value):
        self._list += [value]
        self._length += 1

    def insert(self, key, value):
        if type(key) != int:
            raise TypeError
        if key < 0:
            key += self._length
        if 0 <= key < self._length:
            self._list = self._list[:key] + [value] + self._list[key:]
            self._length += 1
        else:
            raise IndexError

    def pop(self, key=0):
        if type(key) != int:
            raise TypeError
        if key < 0:
            key += self._length
        if 0 <= key < self._length:
            value = self._list[key]
            self._list = self._list[:key] + self._list[key + 1:]
            self._length -= 1
            return value
        else:
            raise IndexError

    def remove(self, value):
        for key, val in enumerate(self):
            if val == value:
                self.pop(key)

    def clear(self):
        self._list = []
        self._length = 0

    def __getitem__(self, item):
        if type(item) != int:
            raise TypeError
        if item < 0:
            item += self._length
        if 0 <= item < self._length:
            return self._list[item]
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if type(key) != int:
            raise TypeError
        if key < 0:
            key += self._length
        if 0 <= key < self._length:
            self._list[key] = value
        else:
            raise IndexError

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self._list)

    def __add__(self, other):
        #list_ = List()
        #list_._list = self._list + other._list
        #list_._length = self._length + other._length
        return List(*self._list, *other._list)

#a = [*list1, *list2]

c = List(1, 2)
b = List(3)
a = c + b
print(a[0], a[1], a[2])
print(len(a))
a.append(5)
print(a)
a.insert(3, 25)
a[1] = 1000
print(a)
a.pop(1)
print(a)
a.remove(25)
print(a)
a.clear()
print(a)

try:
    print(a[5])
except IndexError:
    print("Oops")

print("*" * 30)


class Dictionary:

    def __init__(self, dict):
        self._dict = dict
        self._length = len(dict)

    def get(self, key, default=None):
        if key in self._dict:
            return self._dict[key]
        else:
            return default

    def items(self):
        items = []
        for key in self._dict:
            items.append((key, self._dict[key],))
        return tuple(items)

    def keys(self):
        keys = []
        for key in self._dict:
            keys.append(key)
        return tuple(keys)

    def values(self):
        values = []
        for key in self._dict:
            values.append(self._dict[key])
        return tuple(values)

    def __getitem__(self, item):
        if self.get(item):
            return self._dict[item]
        raise IndexError

    def __setitem__(self, key, value):
        if type(key) != int and type(key) != str:
            raise TypeError
        if key not in self._dict:
            self._length += 1
        self._dict[key] = value

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self._dict)

    def __add__(self, other):
        dictionary = Dictionary(self._dict)
        for i in other._dict:
            dictionary[i] = other[i]
        return dictionary


d = Dictionary({"Name": "Viktor", "Surname": "Tsvil", "Age": 14})
d2 = Dictionary({"Age": 17, "City": "Kyiv"})

d3 = d + d2
print(d3)
print(d3.get("Hair"))
print(d3["Age"])
print(d3.values())
print(d3.keys())
print(d3.items())

