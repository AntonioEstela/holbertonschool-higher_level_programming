#!/usr/bin/python3
import sys
args = sys.argv[1:]
a = 1
if len(args) == 0:
    print("{:d} arguments.".format(len(args)))
else:
    print("{:d} arguments:".format(len(args)))
    for i in args:
        print("{:d}: {}".format(a, i))
        a += 1
