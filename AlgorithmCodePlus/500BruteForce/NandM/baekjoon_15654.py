# https://www.acmicpc.net/problem/15654
# Solved Date: 20.04.12.

import sys
read = sys.stdin.readline


def solved(nums, m, ans, check):
    if m == 0:
        print(' '.join(ans))
        return 0
    for index, number in enumerate(nums):
        if check[index]:
            continue
        ans.append(str(number))
        check[index] = True
        solved(nums, m-1, ans, check)
        check[index] = False
        ans.pop()
    return 0


def main():
    n, m = (int(x) for x in read().split())
    nums = [int(x) for x in read().split()]
    nums.sort()
    ans = []
    check = [False for _ in range(n)]
    solved(nums, m, ans, check)


if __name__ == '__main__':
    main()
