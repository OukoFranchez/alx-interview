#!/usr/bin/python3
""" Minimum Operations Task Module """


from math import sqrt


def minOperations(n):
    """
        Function that computes the minimum operations based on
        the requirements specified above
    """
    if n <= 1:
        return 0

    value = findPrimeFactor(n)
    temp = n
    result = 0
    while value != temp:
        result += value
        temp /= value
        value = findPrimeFactor(temp)

    result += value
    return int(result)


def findPrimeFactor(n):
    """
        Function that finds the lowest prime factor of a number,
        if the number is prime, returns the number itself
    """
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n
