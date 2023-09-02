# pylint: disable=all
"""
*********
 *     *
  *   *
   * *
    *
"""


def func(n, star='*'):
    space = ' '

    for i in range(1, n + 1):
        if i == 1 or i == n:
            # spaces
            for j in range(i - 1):
                print(space, end='')
            # stars
            if i == 1:
                for j in range(2 * n - 1):
                    print(star, end='')
            else:
                print(star, end='')
            # spaces
            for j in range(i - 1):
                print(space, end='')
        else:
            # spaces
            for j in range(i - 1):
                print(space, end='')
            # stars
            print(star, end='')
            # spaces
            for j in range(2 * (n - i) - 1):
                print(space, end='')
            # stars
            print(star, end='')
            # spaces
            for j in range(i - 1):
                print(space, end='')

        print()
