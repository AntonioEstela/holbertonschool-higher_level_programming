#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)
    tuple_sum = tuple(map(sum, zip(tuple_a, tuple_b)))
    return tuple_sum
