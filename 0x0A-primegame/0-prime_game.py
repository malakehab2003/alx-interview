#!/usr/bin/python3
""" implement isWinner function """


def is_prime(n):
    """ check if n is prime """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """ solve prime game problem """
    n = 0
    ben = 0
    maria = 0
    for i in range(x):
        if nums[i] == 0:
            continue
        for j in range(nums[i] + 1):
            if is_prime(j):
                n += 1
        if j == 1:
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
