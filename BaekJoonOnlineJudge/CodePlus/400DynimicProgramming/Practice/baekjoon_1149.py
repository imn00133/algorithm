# https://www.acmicpc.net/problem/1149
# Solve Date: 20.04.02.

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 1000
dp_arr = [[0 for _ in range(3)] for _ in range(MAX)]


def bottom_up(price):
    dp_arr[0] = price[0]
    for i in range(1, len(price)):
        dp_arr[i][0] = min(dp_arr[i-1][1], dp_arr[i-1][2]) + price[i][0]
        dp_arr[i][1] = min(dp_arr[i-1][0], dp_arr[i-1][2]) + price[i][1]
        dp_arr[i][2] = min(dp_arr[i-1][0], dp_arr[i-1][1]) + price[i][2]


def top_down(price, index):
    if index == 0:
        dp_arr[0] = price[0]
        return dp_arr[0]
    if all(dp_arr[index]):
        return dp_arr[index]
    dp_arr[index][0] = min(top_down(price, index-1)[1], top_down(price, index-1)[2]) + price[index][0]
    dp_arr[index][1] = min(top_down(price, index-1)[0], top_down(price, index-1)[2]) + price[index][1]
    dp_arr[index][2] = min(top_down(price, index-1)[0], top_down(price, index-1)[1]) + price[index][2]
    return dp_arr[index]


def main(mode=''):
    house_num = int(read().strip())
    house_price = []
    for _ in range(house_num):
        house_price.append([int(x) for x in read().split()])
    if mode == 'top':
        top_down(house_price, house_num-1)
    else:
        bottom_up(house_price)
    print(min(dp_arr[house_num-1]))


def max_test():
    import random
    house_price = []
    for _ in range(MAX):
        temp = []
        for _ in range(3):
            temp.append(random.randint(1, 1000))
        house_price.append(temp)
    top_down(house_price, MAX-1)
    print(min(dp_arr[MAX-1]))


if __name__ == '__main__':
    main('top')
