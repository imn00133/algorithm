# https://leetcode.com/problems/contiguous-array
# Solved Date: 20.04.14.
# Solution 참고


def find_max_length(nums):
    max_len, sum_count = 0, 0
    count_index = [-2 for _ in range(len(nums) * 2 + 1)]
    count_index[0] = -1
    for index in range(len(nums)):
        if nums[index] == 0:
            sum_count -= 1
        else:
            sum_count += 1
        if count_index[sum_count] < -1:
            count_index[sum_count] = index
        else:
            max_len = max(max_len, index - count_index[sum_count])
    return max_len


def main():
    nums = [int(x) for x in input().split()]
    print(find_max_length(nums))


if __name__ == '__main__':
    main()
