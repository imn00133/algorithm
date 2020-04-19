# https://www.acmicpc.net/problem/14391
# Solved Date: 20.04.19.

import sys
read = sys.stdin.readline


def bit_mask(row, col, paper):
    max_score = 0
    arr_size = row * col
    for index in range(1 << arr_size):
        score = 0
        for y in range(row):
            number = 0
            for x in range(col):
                k = y * row + x
                if index & (1 << k):
                    number = number * 10 + paper[y][x]
                else:
                    score += number
                    number = 0
            score += number
        for x in range(col):
            number = 0
            for y in range(row):
                k = y * row + x
                if index & (1 << k) == 0:
                    number = number * 10 + paper[y][x]
                else:
                    score += number
                    number = 0
            score += number
        max_score = max(max_score, score)
    return max_score


def main():
    row, col = (int(x) for x in read().split())
    paper = []
    for _ in range(row):
        paper.append([int(x) for x in list(read().strip())])
    print(bit_mask(row, col, paper))


if __name__ == '__main__':
    main()
