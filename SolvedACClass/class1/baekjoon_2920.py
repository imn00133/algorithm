# https://www.acmicpc.net/problem/2920
# Solved Date: 20.04.04.

import sys
read = sys.stdin.readline


def main():
    read_order = [int(x) for x in read().split()]
    order = [x for x in range(1, 9)]
    if read_order == order:
        print("ascending")
    elif read_order == list(reversed(order)):
        print("descending")
    else:
        print("mixed")


if __name__ == '__main__':
    main()
