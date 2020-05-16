# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Solved Date: 20.05.15.


class Solution:
    def max_subarray_sum_circular(self, A):
        sub_max = A[0]
        max_sum = A[0]
        sub_min = A[0]
        min_sum = A[0]
        total_sum = A[0]

        for num in A[1:]:
            total_sum += num

            sub_max = max(num, sub_max + num)
            sub_min = min(num, sub_min + num)

            max_sum = max(max_sum, sub_max)
            min_sum = min(min_sum, sub_min)

        if total_sum - min_sum > max_sum > 0:
            return total_sum - min_sum
        else:
            return max_sum


def main():
    solution = Solution()
    nums = [1, 2, -8, 2, 5, -8, 5, 6]
    print(solution.max_subarray_sum_circular(nums))


if __name__ == '__main__':
    main()
