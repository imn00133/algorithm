#
# Solved Date: 20.05.10.


class Solution:
    def is_perfect_square(self, num):
        i = 0
        square = 1
        while square <= num:
            if square == num:
                return True
            i += 1
            square += i * 2 + 1
        return False

    def fast_is_perfect_square(self, num):
        if num == 1:
            return True
        left = 1
        right = num
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if num == square:
                return True
            elif num < square:
                right = mid - 1
            else:
                left = mid + 1
        return False


def main():
    solution = Solution()
    print(solution.fast_is_perfect_square(17))


if __name__ == '__main__':
    main()
