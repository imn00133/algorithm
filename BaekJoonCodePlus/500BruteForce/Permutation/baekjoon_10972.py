# https://www.acmicpc.net/problem/10972
# Solved Date: 20.04.14.

import sys
read = sys.stdin.readline


def next_permutation(nums):
    for index in range(len(nums)-1, 0, -1):
        if nums[index] > nums[index-1]:
            swap_index = 0
            swap_number = len(nums)
            for j in range(index, len(nums)):
                if nums[index-1] < nums[j] <= swap_number:
                    swap_index = j
                    swap_number = nums[j]
            nums[index-1], nums[swap_index] = nums[swap_index], nums[index-1]
            for j in range(index, len(nums)):
                reverse_index = len(nums) - 1 - j + index
                if j > reverse_index:
                    break
                nums[j], nums[reverse_index] = nums[reverse_index], nums[j]
            return True
    return False


def main():
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    if next_permutation(nums):
        print(*nums)
    else:
        print(-1)


if __name__ == '__main__':
    main()
