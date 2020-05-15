# https://www.acmicpc.net/problem/2022
# Solved Date: 20.05.15.

import sys
read = sys.stdin.readline


def main():
    x, y, c = (float(x) for x in read().split())
    x_square = x ** 2
    y_square = y ** 2
    epsilon = 10 ** -6
    left = 0
    right = min(x, y)
    while abs(right - left) > epsilon:
        mid = (left + right) / 2
        d = mid ** 2
        h1 = (x_square - d) ** 0.5
        h2 = (y_square - d) ** 0.5
        if c < h1 * h2 / (h1 + h2):
            left = mid
        else:
            right = mid
    print(f"{left:0.3f}")


if __name__ == '__main__':
    main()
