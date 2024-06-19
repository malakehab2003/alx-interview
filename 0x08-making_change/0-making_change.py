#!/usr/bin/python3
""" solve make change problem as interview """


def get_max(arr):
    if len(arr) <= 0:
        return -1
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


def makeChange(coins, total):
    """ determine the fewest number of coins """
    coin = 0
    if total <= 0:
        return 0
    while total > 0:
        max = get_max(coins)
        if max == -1:
            break
        if max > total:
            coins.remove(max)
            continue
        coin += 1
        total -= max

    if total == 0:
        return coin
    return -1
