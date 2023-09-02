# pylint: disable=all
"""
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""


def func(n, star='*'):
    space = ' '

    for i in range(1, 2 * n):
        if i == 1 or i == 2 * n - 1:
            # spaces
            for j in range(n - 1):
                print(space, end='')
            # stars
            print(star, end='')
            # spaces
            for j in range(n - 1):
                print(space, end='')
        elif i <= n:
            # spaces
            for j in range(n - i):
                print(space, end='')
            # stars
            print(star, end='')
            # spaces
            for j in range(2 * i - 3):
                print(space, end='')
            # stars
            print(star, end='')
            # spaces
            for j in range(n - i):
                print(space, end='')
        else:
            # spaces
            for j in range(i - n):
                print(space, end='')
            # stars
            print(star, end='')
            # spaces
            for j in range(2 * (2 * n - i) - 3):
                print(space, end='')
            # stars
            print(star, end='')
            # spaces
            for j in range(i - n):
                print(space, end='')

        print()
