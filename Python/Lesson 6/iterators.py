import random


list1 = [1, 2, 3, 4, 5]

iterator = iter(list1)

print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator = iter(list1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print('*'*50)


class RandomGeneratorIterator:

    def __init__(self, random_generator_instance):
        self._instance = random_generator_instance
        self._instance._start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._instance._start < self._instance._count:
            self._instance._start += 1
            return random.randint(0, 100)
        raise StopIteration


class RandomGenerator:

    def __init__(self, count):
        self._count = count
        self._start = 0

    def __iter__(self):
        return RandomGeneratorIterator(self)




randgen = RandomGenerator(4)
iterator = iter(randgen)
for i in randgen:
    for j in randgen:
        print(j)
    print(str(i) + " ~")