# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Solved Date: 20.05.08.


class Solution:
    def check_straight_line(self, coordinates):
        try:
            a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            b = coordinates[0][1] - a * coordinates[0][0]
            epsilon = 10 ** -4
            for x, y in coordinates:
                if abs(a * x + b - y) > epsilon:
                    return False
            return True
        except ZeroDivisionError:
            b = coordinates[0][1]
            epsilon = 10 ** -4
            for x, y in coordinates:
                if abs(b - y) > epsilon:
                    return False
            return True


def main():
    solution = Solution()
    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    print(solution.check_straight_line(coordinates))


if __name__ == '__main__':
    main()
