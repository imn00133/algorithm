# https://www.acmicpc.net/problem/1080
# Solved Date: 20.05.09.

import sys
read = sys.stdin.readline

CHANGE = 3


def flip(problem, y, x):
    for dy in range(CHANGE):
        for dx in range(CHANGE):
            problem[y+dy][x+dx] ^= 1


def check(problem, answer):
    for y in range(len(problem)):
        for x in range(len(problem[0])):
            if problem[y][x] != answer[y][x]:
                return False
    return True


def main():
    row, column = (int(x) for x in read().split())
    problem = [[int(x) for x in read().strip()] for _ in range(row)]
    answer = [[int(x) for x in read().strip()] for _ in range(row)]
    count = 0
    for y in range(row - CHANGE + 1):
        for x in range(column - CHANGE + 1):
            if problem[y][x] != answer[y][x]:
                count += 1
                flip(problem, y, x)
    if check(problem, answer):
        print(count)
    else:
        print(-1)


if __name__ == '__main__':
    main()
