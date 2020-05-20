# https://www.acmicpc.net/problem/1783
# Solved Date: 20.05.20.

import sys
read = sys.stdin.readline


def main():
    height, width = (int(x) for x in read().split())
    if height == 1:
        print(1)
    elif height == 2:
        print(min(4, (width + 1) // 2))
    elif width < 7:
        print(min(4, width))
    else:
        print(width - 2)


if __name__ == '__main__':
    main()
