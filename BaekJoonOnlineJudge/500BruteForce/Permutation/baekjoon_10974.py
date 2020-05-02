# https://www.acmicpc.net/problem/10974
# Solved Date: 20.04.15.


def pythonic(nums):
    import itertools
    return itertools.permutations(nums)


def next_permutation(nums):
    index = 0
    for i in range(len(nums)-1, 0, -1):
        if nums[i] > nums[i-1]:
            index = i
            break
    swap_index = 0
    swap_num = len(nums)
    for i in range(index, len(nums)):
        if nums[index-1] < nums[i] <= swap_num:
            swap_index = i
            swap_num = nums[i]
    nums[index-1], nums[swap_index] = nums[swap_index], nums[index-1]
    for i in range(index, len(nums)):
        end_num = len(nums) - 1 - i + index
        if i > end_num:
            break
        else:
            nums[i], nums[end_num] = nums[end_num], nums[i]
    # index가 0이면, 다음이 없음을 나타낸다.
    if index:
        return True
    else:
        return False


def main(mode=''):
    num = int(input())
    nums = [x for x in range(1, num+1)]
    if mode == 'pythonic':
        permutation = pythonic(nums)
        for value in permutation:
            print(*value)
    else:
        print(*nums)
        while next_permutation(nums):
            print(*nums)


if __name__ == '__main__':
    main()
