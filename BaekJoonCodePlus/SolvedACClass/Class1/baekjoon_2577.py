# https://www.acmicpc.net/problem/2577
# Solved Date: 20.04.03.

import sys
read = sys.stdin.readline


def solve(num):
    num = str(num)
    for i in range(10):
        print(num.count(str(i)))


def main():
    num = 1
    for _ in range(3):
        num *= int(read().strip())
    solve(num)


if __name__ == '__main__':
    main()
