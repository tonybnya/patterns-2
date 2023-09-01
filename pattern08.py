# pylint: disable=all
"""
    *
   ***
  *****
 *******
*********
"""


def func(n, star='*'):
    space = ' '

    for i in range(1, n + 1):
        # spaces
        for j in range(n - i):
            print(space, end='')
        # stars
        for j in range(2 * i - 1):
            print(star, end='')
        # spaces
        for j in range(n - i):
            print(space, end='')

        print()


n = 5
func(n)
