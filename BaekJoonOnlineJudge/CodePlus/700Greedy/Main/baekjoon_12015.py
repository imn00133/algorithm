# https://www.acmicpc.net/problem/12015
# Solved Date: 20.05.17.

import sys
import bisect
read = sys.stdin.readline


def index(ans, number):
    left = 0
    right = len(ans) - 1
    while left < right:
        mid = (left + right) // 2
        if ans[mid] < number:
            left = mid + 1
        else:
            right = mid
    return left


def greedy(arr, find_index):
    ans = [arr[0]]
    for number in arr:
        if number > ans[-1]:
            ans.append(number)
        else:
            ans[find_index(ans, number)] = number
    return len(ans)


def main(mode=''):
    arr_num = int(read().strip())
    arr = [int(x) for x in read().split()]
    if mode == 'make':
        find_index = index
    else:
        find_index = bisect.bisect_left
    print(greedy(arr, find_index))


if __name__ == '__main__':
    main()
