#!/usr/bin/python3
def uppercase(str):
    for i in str:
        check = ord(i)
        if check >= 97 and check <= 122:
            check -= 32
        print("{:c}".format(check), end='')
    print(end='\n')
