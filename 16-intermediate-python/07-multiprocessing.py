import multiprocessing

def some_process(num,num2):
    print("in some_process", num, num2)


if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=some_process , args=(i,i+1))
        p.start()
        p.join()