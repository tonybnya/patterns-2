# pylint: disable=all
"""
*****
*****
*****
*****
*****
"""


def func(n, star='*'):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(star, end='')
        print()
