#!/usr/bin/python3
""" Make function take a number and return n of operations """


def minOperations(n: int) -> int:
    """ Return the min number of operations """
    if n <= 1:
        return 0
    count: int = 0
    noOfH: int = 1
    step: int = 1
    while True:
        if noOfH == n:
            return count
        if n % noOfH == 0:
            step = noOfH
            count += 2
        else:
            count += 1
        noOfH += step
