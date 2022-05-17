# https://www.hackerrank.com/contests/kakao-adtech-devday-1st-codejam/challenges/2022-12
# Solved Date: 22.04.14.

import sys
from collections import Counter

read = sys.stdin.readline


def calc_value(bid_floor, prices):
    sum_price = 0
    for price in prices:
        if price < bid_floor:
            continue
        sum_price += bid_floor
    return sum_price


def binary_explorer(prices):
    left = 1
    right = 5000
    left_sum_price = calc_value(1, prices)
    right_sum_price = calc_value(5000, prices)
    while left < right:
        mid = (left + right) // 2
        mid_sum_price = calc_value(mid, prices)
    return right


def simple_solve(prices):
    counter = Counter(prices)
    prices_sort = sorted(counter.keys())
    max_price = 5000 * len(prices_sort)
    for bid_floor in range(1, 5001):
        counter[bid_floor]


def solve():
    num = int(read().rstrip())
    prices = []
    for _ in range(num):
        price = int(read().rstrip())
        if price >= 5000:
            price = 5000
        prices.append(price)
    return simple_solve(prices)


if __name__ == '__main__':
    print(solve())
