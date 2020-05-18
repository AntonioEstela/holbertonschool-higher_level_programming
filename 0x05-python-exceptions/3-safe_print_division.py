#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(res))
    return res
