# https://www.acmicpc.net/problem/11055
# Solved Date:

import sys
read = sys.stdin.readline

dp_arr = [0 for x in range(1000)]


def bottom_up(nums):
    for index, number in enumerate(nums):
        dp_arr[index] = number
        for i in range(index):
            if nums[i] < number and dp_arr[i] + number > dp_arr[index]:
                dp_arr[index] = dp_arr[i] + number


def top_down(nums, i):
    pass


def main(mode=''):
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    if mode == 'top':
        top_down(nums, arr_num-1)
    else:
        bottom_up(nums)
    print(max(dp_arr))


if __name__ == '__main__':
    main('top')
