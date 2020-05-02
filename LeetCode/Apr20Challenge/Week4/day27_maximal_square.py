# https://leetcode.com/problems/maximal-square/
# Solved Date: 20.04.27.


def small_memory_maximal_square(matrix):
    if not matrix:
        return 0
    dp_arr = [0 for _ in range(len(matrix[0]) + 1)]
    max_len = 0
    for i in range(len(matrix)):
        prev = 0
        for j in range(len(matrix[0])):
            temp = dp_arr[j+1]
            if matrix[i][j] == '1':
                dp_arr[j+1] = min(dp_arr[j], dp_arr[j+1], prev) + 1
                max_len = max(max_len, dp_arr[j+1])
            else:
                dp_arr[j+1] = 0
            prev = temp
    return max_len ** 2


def fast_maximal_square(matrix):
    if not matrix:
        return 0
    dp_arr = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
    max_len = 0
    for i in range(len(matrix)):
        for j in range((len(matrix[0]))):
            if matrix[i][j] == '1':
                dp_arr[i+1][j+1] = min(dp_arr[i][j], dp_arr[i+1][j], dp_arr[i][j+1]) + 1
                max_len = max(max_len, dp_arr[i+1][j+1])
    return max_len ** 2


def maximal_square(matrix):

    def check_square(i, j, max_arr):
        if i + max_arr > len(matrix) or j + max_arr > len(matrix[0]):
            return max_arr
        for new_i in range(i, i+max_arr):
            for new_j in range(j, j+max_arr):
                if matrix[new_i][new_j] == '0':
                    return max_arr
        while True:
            end_i = i + max_arr
            end_j = j + max_arr
            if end_i >= len(matrix) or end_j >= len(matrix[0]):
                return max_arr
            for new_i in range(i, end_i+1):
                if matrix[new_i][end_j] == '0':
                    return max_arr
            for new_j in range(j, end_j+1):
                if matrix[end_i][new_j] == '0':
                    return max_arr
            max_arr += 1

    max_arr = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                if max_arr == 0:
                    max_arr += 1
                max_arr = check_square(i, j, max_arr)
        if i + max_arr > len(matrix):
            break
    return max_arr ** 2


def main():
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "1", "1", "1"]]
    print(small_memory_maximal_square(matrix))


if __name__ == '__main__':
    main()

