# https://www.acmicpc.net/problem/10819
# Solved Date: 20.04.15.

import sys
read = sys.stdin.readline


def permutation(nums):
    import itertools
    max_num = 0
    for order in itertools.permutations(nums):
        part_sum = 0
        for index in range(len(order)-1):
            part_sum += abs(order[index] - order[index+1])
        max_num = max(max_num, part_sum)
    return max_num


def main():
    arr_num = int(read().strip())
    nums = [int(x) for x in read().split()]
    nums.sort()
    print(permutation(nums))


if __name__ == '__main__':
    main()
