# https://www.acmicpc.net/problem/2138
# Solved Date: 20.05.10.

import sys
import math
read = sys.stdin.readline


def flip(judge, x, count=3):
    for dx in range(count):
        judge[x+dx] = not judge[x+dx]


def switch_push(judge):
    count = 0
    for index in range(len(judge) - 2):
        if not judge[index]:
            count += 1
            flip(judge, index)
    if not judge[-2]:
        count += 1
        flip(judge, -2, 2)
    if judge[-1]:
        return count
    else:
        return math.inf


def main():
    bulb_num = int(read().strip())
    problem = [int(x) for x in read().strip()]
    answer = [int(x) for x in read().strip()]
    judge = [x == y for x, y in zip(problem, answer)]
    # 처음 안 눌렀을 때
    count = switch_push(judge)
    # 처음 눌렀을 때
    judge = [x == y for x, y in zip(problem, answer)]
    flip(judge, 0, 2)
    count = min(count, switch_push(judge) + 1)
    if count == math.inf:
        print(-1)
    else:
        print(count)


if __name__ == '__main__':
    main()
