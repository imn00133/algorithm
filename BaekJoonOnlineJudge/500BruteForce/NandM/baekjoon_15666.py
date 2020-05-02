# https://www.acmicpc.net/problem/15666
# Solved Date: 20.04.14.

import sys
read = sys.stdin.readline


def solved(m, nums, ans, start=0):
    if m == 0:
        print(' '.join(ans))
        return 0
    for index in range(start, len(nums)):
        ans.append(str(nums[index]))
        solved(m-1, nums, ans, index)
        ans.pop()
    return 0


def main():
    n, m = (int(x) for x in read().split())
    nums = [int(x) for x in read().split()]
    nums = list(set(nums))
    nums.sort()
    ans = []
    solved(m, nums, ans)


if __name__ == '__main__':
    main()
