import threading
import time

start = time.perf_counter()

def do_something(second):
    print(f"sleeping for {second} sec")
    time.sleep(second)
    print(f"done sleeping for {second} sec")

threads =[]
for _ in range(10):
    t = threading.Thread(target=do_something , args=[2])
    t.start()
    threads.append(t)

for i in range(10):
    threads[i].join()


finish = time.perf_counter()

print('finished in' , finish -start , 'sec')