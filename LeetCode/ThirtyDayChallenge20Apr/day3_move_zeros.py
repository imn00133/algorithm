# https://leetcode.com/problems/move-zeroes/
# Solved Date: 20.04.05.

import sys
read = sys.stdin.readline


def fast_move_zero(nums):
    zi = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zi], nums[i] = nums[i], nums[zi]
            zi += 1
    return nums


def move_zeros(nums):
    zero_pointer = 0
    while True:
        for i in range(zero_pointer, len(nums)):
            zero_pointer = i
            if nums[i] == 0:
                break
        num_pointer = zero_pointer
        for _ in range(num_pointer, len(nums)-1):
            num_pointer += 1
            if nums[num_pointer] != 0:
                break
        nums[zero_pointer], nums[num_pointer] = nums[num_pointer], nums[zero_pointer]
        if num_pointer == len(nums) - 1 or zero_pointer == len(nums) - 1:
            break
    return nums


def main():
    nums = [int(x) for x in read().split()]
    print(fast_move_zero(nums))
    print(move_zeros(nums))


if __name__ == '__main__':
    main()
