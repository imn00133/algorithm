# https://www.acmicpc.net/problem/1182
# Solved Date: 20.04.18.

import sys
read = sys.stdin.readline


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
    else:
        print(combination(expected_num, arr))


if __name__ == '__main__':
    main('bit')
