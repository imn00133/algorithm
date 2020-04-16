# https://www.acmicpc.net/problem/6603
# Solved Date: 20.04.15.

import sys
read = sys.stdin.readline

SELECT_NUM = 6


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


def permutation(choice_list):
    main_index = 0
    for index in range(len(choice_list)-1, 0, -1):
        if choice_list[index] < choice_list[index-1]:
            main_index = index
            break
    swap_index = -1
    for index in range(main_index, len(choice_list)):
        if choice_list[index] == 0 and swap_index < index:
            swap_index = index
    choice_list[main_index-1], choice_list[swap_index] = choice_list[swap_index], choice_list[main_index-1]
    for index in range(main_index, len(choice_list)):
        j = len(choice_list) + main_index - index - 1
        if index > j:
            break
        choice_list[index], choice_list[j] = choice_list[j], choice_list[index]
    if main_index:
        return True, choice_list
    else:
        return False, choice_list


def permutation_brute_force(nums):
    choice_list = [0 for _ in range(len(nums))]
    for index in range(SELECT_NUM):
        choice_list[index] = 1
    while True:
        ans = []
        for index in range(len(choice_list)):
            if choice_list[index] == 1:
                ans.append(nums[index])
            if len(ans) == SELECT_NUM:
                break
        print(*ans)
        flag, choice_list = permutation(choice_list)
        if not flag:
            break


def main(mode=''):
    while True:
        arr_num, *nums = [int(x) for x in read().split()]
        if not arr_num:
            break
        if mode == 'p':
            permutation_brute_force(nums)
        else:
            ans = []
            recursion(SELECT_NUM, nums, ans)
        print()


if __name__ == '__main__':
    main('p')
