# https://leetcode.com/problems/subarray-sum-equals-k
# Solved Date: 20.04.23.


def subarray_sum(nums, k):
    sum_dic = {0: 1}
    arr_sum = 0
    count = 0

    for index in range(len(nums)):
        arr_sum += nums[index]
        if arr_sum - k in sum_dic:
            count += sum_dic[arr_sum - k]
        if arr_sum in sum_dic:
            sum_dic[arr_sum] += 1
        else:
            sum_dic[arr_sum] = 1
    return count


def main():
    k = int(input())
    nums = [int(x) for x in input().split()]
    print(subarray_sum(nums, k))


if __name__ == '__main__':
    main()
