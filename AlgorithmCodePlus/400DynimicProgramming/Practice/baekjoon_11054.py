# https://www.acmicpc.net/problem/11054
# Solved Date: 20.04.08.

import sys
read = sys.stdin.readline

MAX = 1000
dp_arr = [[1 for _ in range(2)] for _ in range(MAX)]


def increasing_bottom_up(nums):
    for index, number in enumerate(nums):
        for j in range(index):
            if nums[j] < number and dp_arr[j][0] + 1 > dp_arr[index][0]:
                dp_arr[index][0] = dp_arr[j][0] + 1


def decreasing_bottom_up(nums):
    max_dp = 0
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(nums)-1, i, -1):
            if nums[j] < nums[i] and dp_arr[j][1] + 1 > dp_arr[i][1]:
                dp_arr[i][1] = dp_arr[j][1] + 1
        if max_dp < dp_arr[i][0] + dp_arr[i][1]:
            max_dp = dp_arr[i][0] + dp_arr[i][1]
    return max_dp - 1


def bottom_up(nums):
    increasing_bottom_up(nums)
    ans = decreasing_bottom_up(nums)
    return ans


def main():
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    print(bottom_up(nums))


if __name__ == '__main__':
    main()
