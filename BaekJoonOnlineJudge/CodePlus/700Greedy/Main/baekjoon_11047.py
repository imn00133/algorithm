# https://www.acmicpc.net/problem/11047
# Solved Date: 20.05.08.

import sys
read = sys.stdin.readline


def greedy(value, moneys):
    count = 0
    for money in moneys:
        count += value // money
        value %= money
    return count


def main():
    kind, value = (int(x) for x in read().split())
    moneys = []
    for _ in range(kind):
        moneys.append(int(read().strip()))
    print(greedy(value, sorted(moneys, reverse=True)))


if __name__ == '__main__':
    main()
