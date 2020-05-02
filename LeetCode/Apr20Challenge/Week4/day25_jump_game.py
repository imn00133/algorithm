# https://leetcode.com/problems/jump-game/
# Solved Date: 20.04.25.


def fast_can_jump(nums):
    # https://leetcode.com/problems/jump-game/discuss/596266/Python-simple-O(N)-time-O(1)-space-solution
    max_pos = 0
    for index in range(len(nums)):
        max_pos = max(max_pos, index + nums[index])
        if max_pos == index or max_pos >= len(nums) - 1:
            break
    return max_pos >= len(nums) - 1


def can_jump(nums):
    # dp와 비슷하나, time out남
    possible = {}
    for index in range(len(nums)-1, -1, -1):
        length = len(nums) - 1 - index
        for jump in range(nums[index] + 1):
            if jump == length:
                possible[length] = 1
                break
            elif length - jump in possible:
                possible[length] = 1
                break
    if len(nums) - 1 in possible:
        return True
    else:
        return False


def main():
    nums = [int(x) for x in input().split()]
    print(fast_can_jump(nums))


if __name__ == '__main__':
    main()
