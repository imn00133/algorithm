# https://leetcode.com/problems/majority-element
# Solved Date: 20.05.07.

import collections


def majority_element(nums):
    counter = collections.Counter(nums)
    majority = len(nums) // 2 + 1
    for num in nums:
        if counter[num] >= majority:
            return num


def majority_element_boyer_moore(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
