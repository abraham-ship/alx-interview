#!/usr/bin/python3
'''minimum operations of copy paste'''


def minOperations(n):
    if n <= 1:
        return 0

    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    return sum(factors)
