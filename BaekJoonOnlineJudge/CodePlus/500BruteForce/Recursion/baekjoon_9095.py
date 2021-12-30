# https://www.acmicpc.net/problem/9095
# Solved Date: 20.04.16.

import sys
sys.setrecursionlimit(10 ** 4)
read = sys.stdin.readline

MAX_NUM = 12
dp_arr = [0 for _ in range(MAX_NUM+1)]


def recursion(num):
    if num == 0:
        return 1
    if num < 0:
        return 0
    count = recursion(num-1)
    count += recursion(num-2)
    count += recursion(num-3)
    return count


def bottom_up(num):
    dp_arr[0] = dp_arr[1] = 1
    dp_arr[2] = 2
    for index in range(3, num+1):
        dp_arr[index] = dp_arr[index-1] + dp_arr[index-2] + dp_arr[index-3]
    return dp_arr[num]


def top_down(num):
    if num == 0 or num == 1:
        return 1
    if num == 2:
        return 2
    if dp_arr[num] > 0:
        return dp_arr[num]
    dp_arr[num] = top_down(num-1) + top_down(num-2) + top_down(num-3)
    return dp_arr[num]


def main(mode=''):
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        num = int(read().strip())
        if mode == 'top':
            print(top_down(num))
        elif mode == 'brute':
            print(recursion(num))
        else:
            print(bottom_up(num))


if __name__ == '__main__':
    main('brute')
