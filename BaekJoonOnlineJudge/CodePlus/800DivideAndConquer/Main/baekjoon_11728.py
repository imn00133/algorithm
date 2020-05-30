# https://www.acmicpc.net/problem/11728
# Solved Date: 20.05.30.

import sys
read = sys.stdin.readline


def merge(array1, array2):
    ans = []
    pointer1, pointer2 = 0, 0
    while len(array1) != pointer1 and len(array2) != pointer2:
        if array1[pointer1] < array2[pointer2]:
            ans.append(array1[pointer1])
            pointer1 += 1
        else:
            ans.append(array2[pointer2])
            pointer2 += 1
    while len(array1) != pointer1:
        ans.append(array1[pointer1])
        pointer1 += 1
    while len(array2) != pointer2:
        ans.append(array2[pointer2])
        pointer2 += 1
    return ans


def fast_merge(array1, array2):
    ans = array1 + array2
    return sorted(ans)


def main(mode=''):
    array1_size, array2_size = (int(x) for x in read().split())
    array1 = [int(x) for x in read().split()]
    array2 = [int(x) for x in read().split()]
    if mode == 'fast':
        print(*fast_merge(array1, array2))
    else:
        print(*merge(array1, array2))


if __name__ == '__main__':
    main('fast')
