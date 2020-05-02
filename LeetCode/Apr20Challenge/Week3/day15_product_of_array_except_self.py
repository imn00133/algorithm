# https://leetcode.com/problems/product-of-array-except-self/
# Solved Date: 20.04.16.


def space_low_product_except_self(nums):
    ans = [1]
    right = 1
    for left in nums[:-1]:
        ans.append(left * ans[-1])
    for index in range(len(nums)-1, -1, -1):
        ans[index] *= right
        right *= nums[index]
    return ans


def product_except_self(nums):
    dp_arr = [[1 for _ in range(2)] for _ in range(len(nums))]
    for index in range(1, len(nums)):
        dp_arr[index][0] = dp_arr[index-1][0] * nums[index-1]
    for rev_index in range(len(nums)-2, -1, -1):
        dp_arr[rev_index][1] = dp_arr[rev_index+1][1] * nums[rev_index+1]
    return [x * y for x, y in dp_arr]


def main(mode=''):
    nums = [int(x) for x in input().split()]
    if mode == 'low':
        ans = product_except_self(nums)
    else:
        ans = space_low_product_except_self(nums)
    print(ans)


if __name__ == '__main__':
    main()
