# https://www.acmicpc.net/problem/1546
# Solved Date: 20.04.03.

import sys
read = sys.stdin.readline


def new_average(score):
    max_score = max(score)
    new_score = [x * 100 / max_score for x in score]
    return sum(new_score) / len(new_score)


def main():
    num = int(read().strip())
    score = [int(x) for x in read().split()]
    print(new_average(score))


if __name__ == '__main__':
    main()
