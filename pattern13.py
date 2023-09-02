# pylint: disable=all
"""
    *
   * *
  *   *
 *     *
*********
"""


def func(n, star='*'):
    space = ' '

    for i in range(1, n + 1):
        if i == 1 or i == n:
            # spaces
            for j in range(n - i):
                print(space, end='')
            # stars
            if i == 1:
                for j in range(i):
                    print(star, end='')
            else:
                for j in range(2 * n - 1):
                    print(star, end='')
            # spaces
            for j in range(n - i):
                print(space, end='')
        else:
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
        print()


n = 4
func(n)
