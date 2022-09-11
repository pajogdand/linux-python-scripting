import argparse
import sys

def cal(args):
    x, y, operation = args
    if operation == 'add':
        return  x+y
    if operation == 'sub':
        return  x-y
    if operation == 'mul':
        return x*y
    if operation == 'div':
        return x/y

def main():
    parser =  argparse.ArgumentParser()
    parser.add_argument('--x' ,type=float, default=1.0,
                        help='what is first number')
    parser.add_argument('--y',type=float,default=1.0,
                        help='what is 2nd number')
    parser.add_argument('operation',type=str,default='add',
                        help='what operation you want to perfrom \
                        add, sub. div, mul')
    args=parser.parse_args()
    sys.stdout.write(str(cal(args)))

if __name__ == "__main__":
    main()