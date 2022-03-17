# 13 DSP/BFS문제 - 경쟁적 전염
# Solved Date: 22.03.17.
# https://www.acmicpc.net/problem/18405
import sys
from collections import deque

read = sys.stdin.readline

DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def solution(array, queue, check_second, answer_x, answer_y):
    while queue:
        x, y, virus, second = queue.popleft()
        if second == check_second + 1:
            break
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if 0 > nx or len(array[0]) <= nx or 0 > ny or len(array) <= ny:
                continue
            if array[ny][nx]:
                continue
            array[ny][nx] = virus
            queue.append((nx, ny, virus, second+1))
    return array[answer_x-1][answer_y-1]


if __name__ == '__main__':
    array_num, virus_num = (int(x) for x in read().split())
    array = []
    queue = deque()
    virus_status = [[] for _ in range(virus_num+1)]
    for y in range(array_num):
        row = [int(tube) for tube in read().split()]
        for x, virus in enumerate(row):
            if not virus:
                continue
            queue.append((x, y, virus, 0))
        array.append(row)
    check_second, answer_x, answer_y = (int(x) for x in read().split())
    print(solution(array, queue, check_second, answer_x, answer_y))
