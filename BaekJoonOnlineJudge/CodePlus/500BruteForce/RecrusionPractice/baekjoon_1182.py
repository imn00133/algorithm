# https://www.acmicpc.net/problem/1182
# Solved Date: 20.05.17.

import sys
sys.setrecursionlimit(10 ** 4)
read = sys.stdin.readline


def recursion(expect_num, arr, index=0, partial_sum=0):
    count = 0
    if index == len(arr):
        if partial_sum == expect_num:
            count += 1
        return count
    count += recursion(expect_num, arr, index+1, partial_sum)
    partial_sum += arr[index]
    count += recursion(expect_num, arr, index+1, partial_sum)
    return count


def bit_mask(expected_num, arr):
    ans = 0
    for index in range(1, (1 << len(arr))):
        number_sum = 0
        for j in range(len(arr)):
            if index & (1 << j):
                number_sum += arr[j]
        if expected_num == number_sum:
            ans += 1
    return ans


def combination(expected_num, arr):
    import itertools
    ans = 0
    for i in range(1, len(arr)+1):
        for numbers in itertools.combinations(arr, i):
            number_sum = sum(numbers)
            if number_sum == expected_num:
                ans += 1
    return ans


def main(mode=''):
    arr_num, expected_num = (int(x) for x in read().split())
    arr = [int(x) for x in read().split()]
    if mode == 'bit':
        print(bit_mask(expected_num, arr))
    elif mode == 'recursion':
        count = recursion(expected_num, arr)
        if not expected_num:
            count -= 1
        print(count)
    else:
        print(combination(expected_num, arr))


if __name__ == '__main__':
    main('recursion')
