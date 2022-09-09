import concurrent.futures
import time

start = time.perf_counter()

def do_something(second):
    print(f"sleeping for {second} sec")
    time.sleep(second)
    return "done sleeping"

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something , 1)
#     f2 = executor.submit(do_something, 2)
#
#     print("f1 = " , f1.result())
#     print("f2 = " , f2.result())
#
# finish = time.perf_counter()
# print('finished in' , finish -start , 'sec')

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(do_something,1) for _ in range(10)]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print('finished in' , finish -start , 'sec')