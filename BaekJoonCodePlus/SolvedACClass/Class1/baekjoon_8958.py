# https://www.acmicpc.net/problem/8958
# Solved Date: 20.04.05.

import sys
read = sys.stdin.readline


def calc_score(result):
    score = 0
    continuous = 0
    for letter in result:
        if letter == 'O':
            continuous += 1
            score += continuous
        else:
            continuous = 0
    return score


def main():
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        result = read().strip()
        print(calc_score(result))


if __name__ == '__main__':
    main()
