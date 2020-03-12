import time
from threading import Thread
from multiprocessing import Process


def sleeping(time_to_sleep):
    #time.sleep(time_to_sleep)
    print("I've woken up")


start = time.time()
sleeping(2)
sleeping(3)
print(time.time()-start)

t = Thread(target=sleeping, args=(2,))
t2 = Thread(target=sleeping, args=(3,))

start = time.time()
t.start()
t2.start()
t.join()
t2.join()

print(time.time()-start)
print("\n\n\n")


def calculate(n):

    a = []
    for i in range(n):
        a.append(i)


start = time.time()
calculate(100)
calculate(100)
print(time.time() - start)

t1 = Process(target=calculate, args=(100,))
t2 = Process(target=calculate, args=(100,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time() - start)


list_of_threads = [Thread(target=time.sleep, args=(i,), daemon=True) for i in range(100)]
for thread in list_of_threads:
    thread.start()

for thread in list_of_threads:
    print(thread.getName())


a = []


def calc(i):
    global a
    a.append(i)


list_of_threads = [Thread(target=calc, args=(i,), daemon=True) for i in range(100)]

for thread in list_of_threads:
    thread.start()

time.sleep(1)
#print(a)


class MyThread(Thread):

    def __init__(self, is_daemon):
        super().__init__(daemon=is_daemon)
        self.result = None

    def run(self):
        time.sleep(3)
        self.result = 3


a = MyThread(False)
a.start()
print(a)