def find_divisialbe(inrange, dev_by):
    print("finding nums in range {} , divisiable by".format(inrange,dev_by))
    located=[]
    for i in range(inrange):
        if i % dev_by == 0:
            located.append(i)
    print("done with nums in range {} , divisiable by".format(inrange, dev_by))
    print("============================================")

def main():
    divs1 = find_divisialbe(5000000000,100)
    divs2 = find_divisialbe(600000, 100)
    divs3 = find_divisialbe(700000, 100)

if __name__ == "__main__":
    main()