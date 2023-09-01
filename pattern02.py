# pylint: disable=all
"""
*
**
***
****
"""


def func(n, star='*'):
    for i in range(1, n + 1):
        # for every row, run the col
        for j in range(1, i + 1):
            # print the stars one the same line
            print(star, end='')
        # when each row is printed, add a newline
        print()


n = 5
func(n)
