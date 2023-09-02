# pylint: disable=all
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""


def func(n, star='*'):
    space = ' '

    for i in range(n):
        # spaces
        for j in range(i):
            print(space, end='')
        # stars
        for j in range(n - i):
            print(star + space, end='')
        # spaces
        for j in range(i):
            print(space, end='')
        print()
