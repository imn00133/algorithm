# https://www.acmicpc.net/problem/6064
# Solved Date: 20.04.06.

import sys
read = sys.stdin.readline


def gcd(m, n):
    while n:
        r = m % n
        m = n
        n = r
    return m


def lcm(m, n):
    return int(m / gcd(m, n) * n)


def brute_force(m, n, x, y):
    # 빨리 건너뛸수록 좋으니 큰 수로 바꾼다.
    # 마지막은 lcm일 때가 마지막이다.
    if m < n:
        m, n = n, m
        x, y = y, x
    x, y = x - 1, y - 1
    for year in range(x, lcm(m, n) + 1, m):
        if year % n == y:
            return year + 1
    return -1


def main():
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        m, n, x, y = (int(x) for x in read().split())
        print(brute_force(m, n, x, y))


if __name__ == '__main__':
    main()
