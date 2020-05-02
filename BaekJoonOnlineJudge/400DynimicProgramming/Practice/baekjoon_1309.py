# https://www.acmicpc.net/problem/1309
# Solved Date: 20.04.03.

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 100000
MOD = 9901
dp_arr = [[0 for _ in range(3)] for _ in range(MAX+1)]


def bottom_up(num):
    dp_arr[0][0] = 1
    for i in range(1, num+1):
        dp_arr[i][0] = (dp_arr[i-1][0] + dp_arr[i-1][1] + dp_arr[i-1][2]) % MOD
        dp_arr[i][1] = (dp_arr[i-1][0] + dp_arr[i-1][2]) % MOD
        dp_arr[i][2] = (dp_arr[i-1][0] + dp_arr[i-1][1]) % MOD


def top_down(num):
    if num == 0:
        dp_arr[0][0] = 1
        return dp_arr[num]
    if all(dp_arr[num]):
        return dp_arr[num]
    dp_arr[num][0] = (top_down(num-1)[0] + top_down(num-1)[1] + top_down(num-1)[2]) % MOD
    dp_arr[num][1] = (top_down(num-1)[0] + top_down(num-1)[2]) % MOD
    dp_arr[num][2] = (top_down(num-1)[0] + top_down(num-1)[1]) % MOD
    return dp_arr[num]


def main(mode=''):
    num = int(read().strip())
    if mode == "top":
        if num > 1000:
            for part_num in range(1000, num+1, 1000):
                top_down(part_num)
        top_down(num)
    else:
        bottom_up(num)
    print(sum(dp_arr[num]) % MOD)


if __name__ == '__main__':
    main('top')
