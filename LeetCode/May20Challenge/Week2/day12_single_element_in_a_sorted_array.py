# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Solved Date: 20.05.13.


class Solution:
    def single_non_duplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid % 2:
                mid -= 1
            if mid == len(nums) - 1:
                return nums[mid]
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            elif nums[mid] == nums[mid-1]:
                right = mid - 2
            else:
                return nums[mid]

    def simple_single_non_duplicate(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid & 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

    def fast_single_non_duplicated(self, nums):
        return sum(set(nums)) * 2 - sum(nums)


def main():
    solution = Solution()
    nums = [1]
    print(solution.simple_single_non_duplicate(nums))


if __name__ == '__main__':
    main()
