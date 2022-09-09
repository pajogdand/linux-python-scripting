import threading
import time

start = time.perf_counter()

def do_something():
    print("sleeping for 1sec")
    time.sleep(1)
    print("done sleeping for 1sec")

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t1.start()

finish = time.perf_counter()

print('finished in' , finish -start , 'sec')