# https://www.acmicpc.net/problem/11057
# Solved Date: 20.04.03.

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 1000
MOD = 10007
dp_arr = [[0 for _ in range(10)] for _ in range(MAX+1)]


def bottom_up(num):
    for i in range(10):
        dp_arr[1][i] = 1
    for i in range(2, num+1):
        for j in range(10):
            for k in range(j, 10):
                dp_arr[i][j] += dp_arr[i-1][k] % MOD


def top_down(num):
    if num == 1:
        dp_arr[1] = [1 for _ in range(10)]
        return dp_arr[num]
    if all(dp_arr[num]):
        return dp_arr[num]
    for i in range(10):
        for j in range(i, 10):
            dp_arr[num][i] += top_down(num-1)[j] % MOD
    return dp_arr[num]


def main(mode=''):
    num = int(read().strip())
    if mode == 'top':
        top_down(num)
    else:
        bottom_up(num)
    print(sum(dp_arr[num]) % MOD)


if __name__ == '__main__':
    main('top')
