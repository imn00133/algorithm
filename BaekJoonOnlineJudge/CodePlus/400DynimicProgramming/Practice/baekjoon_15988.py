# https://www.acmicpc.net/problem/15988
# Solved Date: 20.04.02.

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MOD = 1000000009
MAX = 1000000
dp_arr = [0 for _ in range(MAX+1)]


def bottom_up(num):
    dp_arr[0] = dp_arr[1] = 1
    dp_arr[2] = 2
    for number in range(3, num + 1):
        dp_arr[number] = dp_arr[number-1] + dp_arr[number-2] + dp_arr[number-3]
        dp_arr[number] %= MOD
    return dp_arr[num]


def top_down(num):
    if num == 0 or num == 1:
        dp_arr[num] = 1
        return dp_arr[num]
    if num == 2:
        dp_arr[num] = 2
        return dp_arr[num]
    if dp_arr[num] > 0:
        return dp_arr[num]
    dp_arr[num] = (top_down(num-1) + top_down(num-2) + top_down(num-3)) % MOD
    return dp_arr[num]


def main(mode=''):
    test_case_num = int(read().strip())
    if not mode:
        bottom_up(MAX)
    for _ in range(test_case_num):
        num = int(read().strip())
        if mode == 'top':
            if num > 1000:
                for number in range(1000, num+1, 1000):
                    top_down(number)
            print(top_down(num))
        else:
            print(dp_arr[num])


if __name__ == '__main__':
    main('top')
