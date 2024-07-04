#!/usr/bin/python3
""" implement isWinner function """


def is_prime(n):
    """ check if n is prime """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def isWinner(x, nums):
    """ solve prime game problem """
    n = 0
    ben = 0
    maria = 0
    for i in range(x):
        for j in range(nums[i] + 1):
            if is_prime(j):
                n += 1
        if n == 0:
            ben += 1
        elif n % 2 == 0:
            ben += 1
        else:
            maria += 1
        n = 0
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
