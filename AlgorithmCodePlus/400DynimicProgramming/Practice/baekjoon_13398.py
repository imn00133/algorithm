# https://www.acmicpc.net/problem/13398
# Solved Date: 20.04.08.

import sys
read = sys.stdin.readline

MAX = 100000
dp_arr = [[0 for _ in range(2)] for _ in range(MAX)]


def continue_sum(nums):
    pass


def main():
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    print(continue_sum(nums))


if __name__ == '__main__':
    main()
