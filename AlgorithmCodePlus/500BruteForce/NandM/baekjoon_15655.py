# https://www.acmicpc.net/problem/15655
# Solved Date: 20.04.13.

import sys
read = sys.stdin.readline


def solved(m, ans, nums, index=0):
    if m == 0:
        print(' '.join(ans))
        return 0
    if index == len(nums):
        return 0
    ans.append(str(nums[index]))
    solved(m-1, ans, nums, index+1)
    ans.pop()
    solved(m, ans, nums, index+1)
    return 0


def main():
    n, m = (int(x) for x in read().split())
    nums = [int(x) for x in read().split()]
    nums.sort()
    ans = []
    solved(m, ans, nums)


if __name__ == '__main__':
    main()
