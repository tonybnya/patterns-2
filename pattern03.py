# pylint: disable=all
"""
*****
****
***
**
*
"""


def func(n, star='*'):
    for i in range(n):
        for j in range(n - i):
            print(star, end='')
        print()


n = 5
func(n)
