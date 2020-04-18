# https://www.acmicpc.net/problem/15656
# Solved Date: 20.04.13.
# counter에 대해서는 다음을 참고한다.
# https://excelsior-cjh.tistory.com/94

import sys
import collections
read = sys.stdin.readline


def solved(m, nums, nums_dict, ans):
    if m == 0:
        print(' '.join(ans))
        return 0
    for number in nums:
        if nums_dict[number]:
            ans.append(str(number))
            nums_dict[number] -= 1
            solved(m-1, nums, nums_dict, ans)
            ans.pop()
            nums_dict[number] += 1
    return 0


def main():
    n, m = (int(x) for x in read().split())
    nums = [int(x) for x in read().split()]
    # Counter는 dictionary 처럼 사용 가능
    nums_dict = collections.Counter(nums)
    nums = list(nums_dict.keys())
    nums.sort()
    ans = []
    solved(m, nums, nums_dict, ans)


if __name__ == '__main__':
    main()
