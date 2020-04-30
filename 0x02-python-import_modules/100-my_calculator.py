#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    operators = ['+', '-', '*', '/']
    args = sys.argv[1:]
    if len(args) is not 3:
        print("Usage: ./100-my_calculator.py <a> <op> <b>")
        exit(1)
    n1 = int(args[0])
    n2 = int(args[2])
    op = args[1]
    if op not in operators:
        print("Unknown op. Available ops: +, -, * and /")
        exit(1)
    elif op == '+':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.add(n1, n2)))
    elif op == '-':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.sub(n1, n2)))
    elif op == '*':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.mul(n1, n2)))
    elif op == '/':
        print("{:d} {} {:d} = {:d}".format(n1, op, n2, calc.div(n1, n2)))
