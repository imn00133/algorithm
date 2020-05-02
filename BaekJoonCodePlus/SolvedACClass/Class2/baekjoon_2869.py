# https://www.acmicpc.net/problem/2869
# Solved Date: 20.05.02.

import sys
read = sys.stdin.readline


def main():
    up, down, length = (int(x) for x in read().split())
    count = (length - up) // (up - down)
    remainder = (length - up) % (up - down)
    if remainder == 0:
        count += 1
    else:
        count += 2
    print(count)


if __name__ == '__main__':
    main()
