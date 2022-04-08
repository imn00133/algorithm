# 13 DSP/BFS문제 - 인구 이동
# Solved Date: 22.04.01.
# https://www.acmicpc.net/problem/16234
import sys
from collections import deque

read = sys.stdin.readline
DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def make_union_list(array, no_more_check, check, lower, upper, init_x, init_y):
    union_list = [(init_x, init_y)]
    queue = deque()
    queue.append((init_x, init_y))
    while queue:
        x, y = queue.popleft()
        check_count = 0
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(array[0]) or ny < 0 or ny >= len(array[0]):
                check_count += 1
                continue

            if check[ny][nx]:
                check_count += 1
                continue

            population_diff = abs(array[y][x] - array[ny][nx])
            if population_diff < lower or population_diff > upper:
                continue

            check[ny][nx] = True
            union_list.append((nx, ny))
            queue.append((nx, ny))
        if check_count == 4:
            no_more_check[y][x] = True
    return union_list


def check_union(array, no_more_check, lower, upper):
    check = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    union_lists = []
    for y in range(len(array)):
        for x in range(len(array[0])):
            check[y][x] = True
            if no_more_check[y][x]:
                continue

            union_list = make_union_list(array, no_more_check, check, lower, upper, x, y)
            if len(union_list) == 1:
                continue
            union_lists.append(union_list)
    return union_lists


def connect_union(array, union_lists):
    for union_list in union_lists:
        people_sum = 0
        for x, y in union_list:
            people_sum += array[y][x]

        average_people = people_sum // len(union_list)
        for x, y in union_list:
            array[y][x] = average_people


def solution(array, lower, upper):
    day = 0
    no_more_check = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    while True:
        union_lists = check_union(array, no_more_check, lower, upper)
        if not union_lists:
            break
        connect_union(array, union_lists)
        day += 1
    return day


def main():
    array_num, lower, upper = (int(x) for x in read().split())
    array = []
    for _ in range(array_num):
        array.append([int(x) for x in read().split()])
    print(solution(array, lower, upper))


if __name__ == '__main__':
    main()
