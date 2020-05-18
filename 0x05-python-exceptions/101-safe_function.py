#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    func = None
    try:
        func = fct(*args)
    except BaseException as err:
        print("Exception: {:}".format(err), file=sys.stderr)
    finally:
        return func
