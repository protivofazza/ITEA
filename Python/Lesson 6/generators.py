import random


def random_generator(count):
    start = 0

    while start < count:
        start += 1
        yield random.randint(0, 100)
        print("AFTER YIELD")
        yield random.randint(0, 100)


gen = random_generator(3)

print(next(gen))
print(next(gen))
print(next(gen))

randoms = (random.randint(0, 100) for _ in range(10))  # generator
rans = [random.randint(0, 100) for _ in range(10)]  # comprehension

for i in randoms:
    print(i)
