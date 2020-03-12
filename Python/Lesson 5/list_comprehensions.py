import time


result_list = []

start_loop = time.time()
for i in range(1000000):
    if i % 2 == 0:
        result_list.append(i+1)
    else:
        result_list.append(i-1)
end_loop = time.time() - start_loop

start_compr = time.time()
result_list2 = [i+1 if i % 2 == 0 else i-1 for i in range(1000000)]
end_compr = time.time() - start_compr

print(end_loop/end_compr)


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

compr_dict = {key: value for key, value in zip(a, b)}
print(compr_dict)

for _ in range(5):
    print('Hello World')