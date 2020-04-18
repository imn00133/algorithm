# https://www.acmicpc.net/problem/15656
# Solved Date: 20.04.13.

import sys
read = sys.stdin.readline


def solved(m, nums, ans, index=0):
    if m == 0:
        print(' '.join(ans))
        return 0
    for index in range(index, len(nums)):
        ans.append(str(nums[index]))
        solved(m-1, nums, ans, index)
        ans.pop()
    return 0


def main():
    n, m = (int(x) for x in read().split())
    nums = [int(x) for x in read().split()]
    nums.sort()
    ans = []
    solved(m, nums, ans)


if __name__ == '__main__':
    main()
