# https://www.acmicpc.net/problem/11722
# Solved Date: 20.04.07.

import sys
read = sys.stdin.readline

MAX = 1000
dp_arr = [0 for x in range(MAX)]


def bottom_up(nums):
    # 뒤집어서 증가 수열과 똑같이 푼다.
    for index, number in enumerate(nums):
        for i in range(index):
            if nums[i] < number and dp_arr[i] + 1 > dp_arr[index]:
                dp_arr[index] = dp_arr[i] + 1
        if dp_arr[index] == 0:
            dp_arr[index] = 1


def top_down(nums):
    pass


def main(mode=''):
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    nums.reverse()
    if mode == 'top':
        top_down(nums)
    else:
        bottom_up(nums)
    print(max(dp_arr))


if __name__ == '__main__':
    main()
