# https://www.acmicpc.net/problem/2839
# Solved Date: 20.05.02.

import sys
read = sys.stdin.readline


def main():
    delivery_weight = int(read().strip())
    five_count = delivery_weight // 5
    reminder = delivery_weight % 5
    if reminder == 0:
        three_count = 0
    elif reminder == 1:
        five_count -= 1
        three_count = 2
    elif reminder == 2:
        five_count -= 2
        three_count = 4
    elif reminder == 3:
        three_count = 1
    else:
        five_count -= 1
        three_count = 3
    if five_count < 0:
        print(-1)
    else:
        print(five_count + three_count)


if __name__ == '__main__':
    main()
