# https://www.acmicpc.net/problem/14225
# Solved Date: 20.05.17.

import sys
sys.setrecursionlimit(10 ** 4)

read = sys.stdin.readline


def recursion(arr, ans, index=0, partial_sum=0):
    if index == len(arr):
        ans.add(partial_sum)
        return None
    recursion(arr, ans, index+1, partial_sum)
    partial_sum += arr[index]
    recursion(arr, ans, index+1, partial_sum)
    return None


def recursion_main(arr):
    ans = set()
    recursion(arr, ans)
    index = 0
    while True:
        if index not in ans:
            return index
        else:
            index += 1


def greedy(arr):
    # https://www.acmicpc.net/source/17918992
    # https://peanut2016.tistory.com/225
    arr.sort()
    ans = 1
    for number in arr:
        if number > ans:
            pass
    return len(arr)


def main(mode=''):
    arr_num = int(read().strip())
    arr = [int(x) for x in read().split()]
    if mode == 'recursion':
        print(recursion_main(arr))
    else:
        print(greedy(arr))


if __name__ == '__main__':
    main('recursion')
