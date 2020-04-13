# https://www.acmicpc.net/problem/15656
# Solved Date: 20.04.13.

import sys
read = sys.stdin.readline


def solved(m, ans, nums):
    if m == 0:
        print(' '.join(ans))
        return 0
    for number in nums:
        ans.append(str(number))
        solved(m-1, ans, nums)
        ans.pop()
    return 0


def main():
    n, m = (int(x) for x in read().split())
    nums = [int(x) for x in read().split()]
    nums.sort()
    ans = []
    solved(m, ans, nums)


if __name__ == '__main__':
    main()
