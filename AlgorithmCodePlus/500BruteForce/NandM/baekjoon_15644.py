# https://www.acmicpc.net/problem/15664
# Solved Date: 20.04.14.

import sys
import collections
read = sys.stdin.readline


def solved(m, nums, nums_dict, ans, index=0):
    if m == 0:
        print(' '.join(ans))
        return 0
    for index in range(index, len(nums)):
        number = nums[index]
        if nums_dict[number]:
            ans.append(str(number))
            nums_dict[number] -= 1
            if nums_dict[number]:
                solved(m-1, nums, nums_dict, ans, index)
            else:
                solved(m-1, nums, nums_dict, ans, index+1)
            ans.pop()
            nums_dict[number] += 1
    return 0


def main():
    n, m = (int(x) for x in read().split())
    nums = [int(x) for x in read().split()]
    nums_dict = collections.Counter(nums)
    nums = list(nums_dict.keys())
    nums.sort()
    ans = []
    solved(m, nums, nums_dict, ans)


if __name__ == '__main__':
    main()
