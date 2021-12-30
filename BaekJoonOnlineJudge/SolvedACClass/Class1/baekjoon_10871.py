# https://www.acmicpc.net/problem/10871
# Solving Date: 20.03.29.
# pythonic이 4ms 빠르게 나오나, 오차 범위인 듯 하다.

import sys
read = sys.stdin.readline


def legacy(num_list, x):
    num_filter = []
    for num in num_list:
        if num < x:
            num_filter.append(num)
    return num_filter


def pythonic(num_list, x):
    num_filter = [num for num in num_list if num < x]
    return num_filter


def main():
    arr_num, x = (int(x) for x in read().split())
    num_list = [int(num) for num in read().split()]
    num_filter = legacy(num_list, x)
    for num in num_filter:
        print(num, end=' ')


if __name__ == '__main__':
    main()
