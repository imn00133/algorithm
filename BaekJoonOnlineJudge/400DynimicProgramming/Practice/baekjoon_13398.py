# https://www.acmicpc.net/problem/13398
# Solved Date: 20.04.08.

import sys
read = sys.stdin.readline

MAX = 100000
dp_arr = []


def continue_sum(nums):
    dp = [nums[0]]
    for index, value in enumerate(nums[1:]):
        if dp[index] > 0:
            dp.append(dp[index] + value)
        else:
            dp.append(value)
    return dp


def remove_continue_sum(arr_num, nums):
    # 순방향 연속합
    dp_arr.append(continue_sum(nums))
    # 역방향 연속합
    temp_dp = continue_sum(list(reversed(nums)))
    dp_arr.append(list(reversed(temp_dp)))

    # 제거했을 때 합이 최대가 되는 값을 찾기
    if arr_num == 1:
        max_sum = dp_arr[0][0]
    else:
        max_sum = max(dp_arr[0])
        for index in range(arr_num):
            if index == 0:
                max_sum = max(max_sum, dp_arr[1][index+1])
            elif index == arr_num - 1:
                max_sum = max(max_sum, dp_arr[0][index-1])
            else:
                max_sum = max(max_sum, dp_arr[0][index-1] + dp_arr[1][index+1])
    return max_sum


def main():
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    print(remove_continue_sum(arr_num, nums))


if __name__ == '__main__':
    main()
