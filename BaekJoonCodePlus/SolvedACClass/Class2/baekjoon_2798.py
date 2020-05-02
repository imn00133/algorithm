# https://www.acmicpc.net/problem/2798
# Solved Date: 20.04.09.

import sys
read = sys.stdin.readline


def solve(m, cards, select, i=0, max_sum=0):
    if len(select) == 3:
        temp_sum = sum(select)
        if max_sum < temp_sum <= m:
            max_sum = temp_sum
        return max_sum
    if i >= len(cards):
        return max_sum
    select.append(cards[i])
    max_sum = solve(m, cards, select, i+1, max_sum)
    select.pop()
    max_sum = solve(m, cards, select, i+1, max_sum)
    return max_sum


def main():
    n, m = (int(x) for x in read().split())
    cards = [int(x) for x in read().split()]
    select = []
    print(solve(m, cards, select))


if __name__ == '__main__':
    main()
