# https://www.acmicpc.net/problem/10844
# Solved Date: 20.03.31.

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 100
MOD = 1000000000
dp_arr = [[0 for _ in range(10)] for _ in range(MAX+1)]


def bottom_up(num):
    for i in range(1, 10):
        dp_arr[1][i] = 1
    for index in range(2, num+1):
        for j in range(10):
            if j == 0:
                dp_arr[index][j] = dp_arr[index-1][j+1] % MOD
            elif j == 9:
                dp_arr[index][j] = dp_arr[index-1][j-1] % MOD
            else:
                dp_arr[index][j] = (dp_arr[index-1][j+1] + dp_arr[index-1][j-1]) % MOD
    return sum(dp_arr[num]) % MOD


def calc(num, i):
    if num == 1 or dp_arr[num][i] > 0:
        return dp_arr[num][i]
    if i == 0:
        dp_arr[num][i] = calc(num-1, i+1) % MOD
    elif i == 9:
        dp_arr[num][i] = calc(num-1, i-1) % MOD
    else:
        dp_arr[num][i] = (calc(num-1, i+1) + calc(num-1, i-1)) % MOD
    return dp_arr[num][i]


def top_down(num):
    for i in range(1, 10):
        dp_arr[1][i] = 1
    for i in range(10):
        calc(num, i)
    return sum(dp_arr[num]) % MOD


def main(mode=''):
    num = int(read().strip())
    if mode == 'top':
        print(top_down(num))
    else:
        print(bottom_up(num))


if __name__ == '__main__':
    main('top')
