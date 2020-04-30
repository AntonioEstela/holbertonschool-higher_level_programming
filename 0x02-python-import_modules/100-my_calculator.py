#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    args = sys.argv[1:]
    if len(args) is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    n1 = int(args[0])
    n2 = int(args[2])
    op = args[1]
    if op == '+':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.add(n1, n2)))
    elif op == '-':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.sub(n1, n2)))
    elif op == '*':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.mul(n1, n2)))
    elif op == '/':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.div(n1, n2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
