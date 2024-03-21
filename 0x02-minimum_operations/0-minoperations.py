#!/usr/bin/python3
""" Minimum Operations Task Module """


def minOperations(n):
    """
Calculate the minimum number of operations required to obtain a
string of length 'n' using the following operations:
- Append the current string with its reverse
- Append the current string with a copy of itself

Parameters:
n (int): The length of the desired string

Returns:
int: The minimum number of operations required to obtain the string

Example:
>>> minOperations(5)
3
"""
    if n <= 1:
        return 0

    """
    Initializing an array to store minimum operations
    for each number of characters
    """
    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = float('inf')  # Set initial minimum to infinity
        for j in range(1, i):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)
    return min_ops[n]
