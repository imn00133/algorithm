# https://www.acmicpc.net/problem/6603
# Solved Date: 20.04.15.

import sys
read = sys.stdin.readline


def recursion(m, nums, ans, index=0):
    if m == 0:
        print(*ans)
        return 0
    if len(nums) - index - m < 0:
        return 0
    ans.append(nums[index])
    recursion(m-1, nums, ans, index+1)
    ans.pop()
    recursion(m, nums, ans, index+1)
    return 0


def permutation(nums, choice_list):
    main_index = 0
    for index in range(len(choice_list), 0, -1):
        if choice_list[index] < choice_list[index-1]:
            main_index = index
            break
    swap_index = -1
    for index in range(main_index, len(choice_list)):
        pass
    if main_index:
        return True
    else:
        return False


def main(mode=''):
    while True:
        arr_num, *nums = [int(x) for x in read().split()]
        if not arr_num:
            break
        if mode == 'p':
            choice_list = [0 for _ in range(arr_num)]
            for index in range(6):
                choice_list[index] = 1
            permutation(nums, choice_list)
        else:
            ans = []
            recursion(6, nums, ans)
        print()


if __name__ == '__main__':
    main('p')
