#
# Solved Date: 20.04.20.


def search(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left = mid
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid
            else:
                right = mid

    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


def search_test(nums, target):
    def binary_explore(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= target < nums[mid] or (nums[mid] <= nums[right] and not (nums[mid] < target <= nums[right])):
            right = mid - 1
        else:
            left = mid + 1
        return binary_explore(left, right)
    return binary_explore(0, len(nums) - 1)


def binary_search(nums, target, start, end):
    # https://wayhome25.github.io/cs/2017/04/15/cs-16/
    if start > end:
        return None
    mid = (start + end) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(nums, target, start, end)


def main():
    nums = [int(x) for x in input().split()]
    target = int(input())
    print(search_test(nums, target))


if __name__ == '__main__':
    main()
