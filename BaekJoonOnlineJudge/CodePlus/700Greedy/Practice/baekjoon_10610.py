# https://www.acmicpc.net/problem/10610
# Solved Date: 20.05.20.

import sys
read = sys.stdin.readline


def fast_calc(number):
    # https://www.acmicpc.net/source/13419085 참고
    if sum([int(x) for x in number]) % 3 or number[-1] != '0':
        return -1
    return ''.join(number)


def calc(number):
    if number % 3:
        return -1
    number = list(str(number))
    number.sort(reverse=True)
    if number[-1] != '0':
        return -1
    else:
        return ''.join(number)


def main(mode=''):
    if mode == 'slow':
        number = int(read().strip())
        print(calc(number))
    else:
        number = sorted(read().strip(), reverse=True)
        print(fast_calc(number))


if __name__ == '__main__':
    main()
