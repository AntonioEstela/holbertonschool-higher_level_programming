#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    args = sys.argv[1:]
    if len(args) is not 3:
        print("Usage: ./100-my_calculator.py <a> <op> <b>")
        exit(1)
    num1 = int(args[0])
    num2 = int(args[2])
    op = ord(args[1])
    if op is not 43 and op is not 45 and op is not 42 and op is not 47:
        # Ascii representation of + - * /
        print("Unknown op. Available ops: +, -, * and /")
        exit(1)
    elif op == 43:
        print("{:d} + {:d} = {:d}".format(num1, num2, calc.add(num1, num2)))
    elif op == 45:
        print("{:d} - {:d} = {:d}".format(num1, num2, calc.sub(num1, num2)))
    elif op == 42:
        print("{:d} * {:d} = {:d}".format(num1, num2, calc.mul(num1, num2)))
    elif op == 47:
        print("{:d} / {:d} = {:d}".format(num1, num2, calc.div(num1, num2)))
