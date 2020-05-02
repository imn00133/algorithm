# https://leetcode.com/problems/longest-common-subsequence/
# Solved Date: 20.04.27.


def longest_common_subsequence(text1, text2):
    dp_arr = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i-1] == text2[j-1]:
                dp_arr[i][j] = dp_arr[i-1][j-1] + 1
            else:
                dp_arr[i][j] = max(dp_arr[i-1][j], dp_arr[i][j-1])
    return dp_arr[-1][-1]


def main():
    text1 = "abcde"
    text2 = "ace"
    print(longest_common_subsequence(text1, text2))


if __name__ == '__main__':
    main()
