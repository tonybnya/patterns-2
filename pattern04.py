# pylint: disable=all
"""
1
12
123
1234
12345
"""


def func(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
