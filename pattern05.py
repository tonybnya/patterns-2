# pylint: disable=all
"""
*
**
***
****
*****
****
***
**
*
"""


def func(n, star='*'):
    for i in range(1, 2 * n):
        if i > n:
            for j in range(2 * n - i):
                print(star, end='')
        else:
            for j in range(1, i + 1):
                print(star, end='')
        print()
