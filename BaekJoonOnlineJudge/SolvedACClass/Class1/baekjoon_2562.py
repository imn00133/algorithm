# https://www.acmicpc.net/problem/2562
# Solved Date: 20.04.02.

import sys
read = sys.stdin.readline

MAX = 9


def pythonic():
    nums = []
    for _ in range(MAX):
        nums.append(int(read().strip()))
    max_num = max(nums)
    print(max_num)
    print(nums.index(max_num)+1)


def legacy():
    max_num = 0
    max_index = -1
    for index in range(1, MAX+1):
        num = int(read().strip())
        if num > max_num:
            max_num = num
            max_index = index
    print(max_num)
    print(max_index)


def main(mode=''):
    if mode == 'legacy':
        legacy()
    else:
        pythonic()


if __name__ == '__main__':
    main()
