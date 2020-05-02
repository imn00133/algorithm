# https://www.acmicpc.net/problem/17404
# Solved Date: 20.04.18.

import sys
read = sys.stdin.readline

MAX = 1000
MAX_PRICE = 1000


def condition_fill_up(start, prices):
    dp_arr = [[MAX_PRICE + 1 for _ in range(3)] for _ in range(len(prices))]
    dp_arr[0][start] = prices[0][start]
    for index in range(1, len(prices)):
        dp_arr[index][0] = min(dp_arr[index-1][1], dp_arr[index-1][2]) + prices[index][0]
        dp_arr[index][1] = min(dp_arr[index-1][0], dp_arr[index-1][2]) + prices[index][1]
        dp_arr[index][2] = min(dp_arr[index-1][0], dp_arr[index-1][1]) + prices[index][2]
    cost = []
    for color in range(3):
        if color == start:
            continue
        else:
            cost.append(dp_arr[-1][color])
    return min(cost)


def bottom_up(prices):
    min_cost = MAX * MAX_PRICE + 1
    color = [x for x in range(3)]
    for start in color:
        min_cost = min(min_cost, condition_fill_up(start, prices))
    return min_cost


def main():
    arr_num = int(read().strip())
    prices = []
    for _ in range(arr_num):
        prices.append([int(x) for x in read().split()])
    print(bottom_up(prices))


if __name__ == '__main__':
    main()
