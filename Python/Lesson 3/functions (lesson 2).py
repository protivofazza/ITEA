to_square = lambda x, y: [x ** 2, y ** 2]

list1 = [1,2,3,4]
list2 = [5,6,7,8]
result = map(to_square, list1, list2)
# print(list(result))

result = list(filter(lambda x: not x % 2, list1))
# print(result)

a = [1,2,3]
b = [2,3,4]
c = [5,6,7]

r = zip(a, b, c)
r = list(r)
print(r)