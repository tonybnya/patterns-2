# pylint: disable=all
"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""


def func(n, star='*'):
    space = ' '

    for i in range(1, n + 1):
        if i == 1:
            # spaces
            for j in range(n - i):
                print(space, end='')
            # stars
            print(i, end='')
            # spaces
            for j in range(n - i):
                print(space, end='')
        elif i == n:
            for j in range(1, 2 * n):
                if j == 1 or j == 2 * n - 1:
                    print(1, end='')
                else:
                    print(space, end='')
        else:
            # spaces
            for j in range(n - i):
                print(space, end='')
            # 1
            print(1, end='')
            # spaces
            for j in range(2 * i - 3):
                print(space, end='')
            # 1
            print(1, end='')
            # spaces
            for j in range(n - i):
                print(space, end='')

        print()


n = 5
func(n)
