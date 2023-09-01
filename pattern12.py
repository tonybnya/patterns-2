# pylint: disable=all
"""
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
"""


def func(n, star='*'):
    space = ' '

    for i in range(2 * n - 1):
        if i < n:
            # spaces
            for j in range(i):
                print(space, end='')
            # stars
            for j in range(n - i):
                print(star + space, end='')
            # spaces
            for j in range(i):
                print(space, end='')
        else:
            # spaces
            for j in range():
            # stars
            for j in range(i - n + 1):
                print(star + space, end='')
            # spaces
        print()


n = 5
func(n)
