# https://www.acmicpc.net/problem/15658
# Solved Date: 20.05.17.

import sys
sys.setrecursionlimit(10 ** 6)

read = sys.stdin.readline
MAX = 10 ** 9


def calc(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        if num1 > 0:
            return num1 // num2
        else:
            return - (-num1 // num2)


def recursion(nums, operations, partial_sum, index=0):
    if index == len(nums):
        return partial_sum, partial_sum
    max_num = -MAX
    min_num = MAX
    for select in range(len(operations)):
        if operations[select] > 0:
            operations[select] -= 1
            temp_max, temp_min = recursion(nums, operations, calc(partial_sum, nums[index], select), index+1)
            operations[select] += 1
            if temp_max > max_num:
                max_num = temp_max
            if temp_min < min_num:
                min_num = temp_min
    return max_num, min_num


def main():
    num_arr = int(read().strip())
    nums = tuple(int(x) for x in read().split())
    operations = [int(x) for x in read().split()]
    print(*recursion(nums[1:], operations, nums[0]), sep='\n')


if __name__ == '__main__':
    main()
