#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numbers = sys.argv[1:]
    num = 0
    for i in numbers:
        num += int(i)
    print("{:d}".format(num))
