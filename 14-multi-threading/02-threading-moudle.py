import time

start = time.perf_counter()

def do_something():
    print("sleeping for 1sec")
    time.sleep(1)
    print("done sleeping for 1sec")

do_something()
do_something()
finish = time.perf_counter()

print('finished in' , finish -start , 'sec')