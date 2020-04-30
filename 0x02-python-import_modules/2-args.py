#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    a = 1
    if len(args) == 0:
        print("{:d} arguments.".format(len(args)))
    elif len(args) == 1:
        print("{:d} argument:".format(len(args)))
        print("{:d}: {}".format(a, args[0]))
    else:
        print("{:d} arguments:".format(len(args)))
        for i in args:
            print("{:d}: {}".format(a, i))
            a += 1
