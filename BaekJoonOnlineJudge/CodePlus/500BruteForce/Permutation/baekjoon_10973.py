# https://www.acmicpc.net/problem/10973
# Solved Date: 20.04.15.

import sys
read = sys.stdin.readline


def prev_permutation(nums):
    for index in range(len(nums)-1, 0, -1):
        if nums[index] < nums[index-1]:
            swap_index = 0
            swap_number = 0
            for j in range(index, len(nums)):
                number = nums[j]
                if swap_number < number < nums[index-1]:
                    swap_index = j
                    swap_number = number
            nums[index-1], nums[swap_index] = nums[swap_index], nums[index-1]
            for j in range(index, len(nums)):
                end_index = len(nums) - 1 - j + index
                if j > end_index:
                    break
                nums[j], nums[end_index] = nums[end_index], nums[j]
            return True
    return False


def main():
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    if prev_permutation(nums):
        print(*nums)
    else:
        print(-1)


if __name__ == '__main__':
    main()
