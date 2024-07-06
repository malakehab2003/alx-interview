#!/usr/bin/python3
""" implement isWinner function """


def sieve_of_eratosthenes(max_n):
    """ get only prime numbers """
    is_prime = [True] * (max_n + 1)
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """ get the winner of maria and ben """
    if x == 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def count_primes_up_to(n):
        """ return count of prime numbers less than n """
        count = 0
        for p in primes:
            if p > n:
                break
            count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = count_primes_up_to(n)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
