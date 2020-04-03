# https://leetcode.com/problems/maximum-subarray/
# Solved Date: 20.04.03.

import sys
read = sys.stdin.readline


def max_sub_array(nums):
    dp_arr = []
    for num in nums:
        if not dp_arr:
            dp_arr.append(num)
            continue
        if dp_arr[-1] > 0:
            dp_arr.append(dp_arr[-1] + num)
        else:
            dp_arr.append(num)
    return max(dp_arr)


def main():
    nums = [int(x) for x in read().split()]
    print(max_sub_array(nums))


if __name__ == '__main__':
    main()
