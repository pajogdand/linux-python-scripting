import time
import threading

def sum_of_sqaures(numbers):
    ret = 0
    for i in numbers:
        time.sleep(0.2)
        ret = ret + i*i

    print("result" , ret)


def sum_of_qubes(numbers):
    ret = 0
    for i in numbers:
        time.sleep(0.2)
        ret = ret + i * i *i

    print("result", ret)

t = time.time()
numbers = [12,12,1,4323,42,234234,234,234,234,2,34,23,4234,234,23]
t1 = threading.Thread(target=sum_of_sqaures , args=(numbers,))
t2 = threading.Thread(target=sum_of_qubes , args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()
print("time elapased ",time.time()-t )


