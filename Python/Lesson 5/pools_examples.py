from concurrent.futures import ThreadPoolExecutor, as_completed
import time

executor = ThreadPoolExecutor(max_workers=100)


def sleeping(time_to_sleep):
    time.sleep(time_to_sleep)
    return time_to_sleep


a = []
for i in range(100):
    a.append(executor.submit(sleeping, 100-i))

for result in as_completed(a):
    print(result.result())