# 13 DSP/BFS문제 - 인구 이동
# Solved Date: 22.04.01.
# https://www.acmicpc.net/problem/16234
import sys
from collections import deque

read = sys.stdin.readline
DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def is_in_union_list(new_territory, union_list):
    for union_x, union_y in union_list:
        if new_territory is array[union_y][union_x]:
            return True
    return False


def make_union_list(array, check, lower, upper, init_x, init_y):
    union_list = [(init_x, init_y)]
    queue = deque()
    queue.append((init_x, init_y))
    while queue:
        x, y = queue.popleft()
        self_territory = array[y][x]
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(array[0]) or ny < 0 or ny >= len(array[0]):
                continue

            if check[ny][nx]:
                continue

            new_territory = array[ny][nx]
            if is_in_union_list(new_territory, union_list):
                continue

            population_diff = abs(self_territory[1] - new_territory[1])
            if population_diff < lower or population_diff > upper:
                continue

            check[ny][nx] = True
            union_list.append((nx, ny))
            queue.append((nx, ny))
    return union_list


def check_union(array, lower, upper):
    check = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    union_lists = []
    for y in range(len(array)):
        for x in range(len(array[0])):
            check[y][x] = True
            union_list = make_union_list(array, check, lower, upper, x, y)
            if len(union_list) == 1:
                continue
            union_lists.append(union_list)
    return union_lists


def connect_union(array, union_lists):
    for union_list in union_lists:
        union_status = [0, 0]
        for x, y in union_list:
            territory_status = array[y][x]
            union_status[0] += territory_status[0]
            union_status[1] += territory_status[1]
            array[y][x] = union_status
        union_status[1] = union_status[1] // union_status[0]


def solution(array, lower, upper):
    day = 0
    while True:
        union_lists = check_union(array, lower, upper)
        if not union_lists:
            break
        connect_union(array, union_lists)
        day += 1
    return day


# 1. 연합은 한 번 만들어지면 연결됨
# -> 따라서 한 번 연결되면 경계선만 확인하면 됨
# -> 더 이상 확인하지 않을 부분을 만들어서 True, False로 둠
# 2. 연합은 동일성 비교로 확인
# -> 연합을 넣을 때, 연합을 만들려는 값이랑 같은지 확인하는 부분이 필요
if __name__ == '__main__':
    array_num, lower, upper = (int(x) for x in read().split())
    array = []
    for _ in range(array_num):
        array.append([[1, int(x)] for x in read().split()])
    print(solution(array, lower, upper))

#
# # 13 DSP/BFS문제 - 인구 이동
# # Solved Date: 22.03.31.
# # https://www.acmicpc.net/problem/16234
# import sys
# from collections import deque
#
# read = sys.stdin.readline
# DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))
#
#
# def is_in_union_list(new_territory, union_list):
#     for union_x, union_y in union_list:
#         if new_territory is array[union_y][union_x]:
#             return True
#     return False
#
#
# def make_union(array, territory, check, lower, upper, init_x, init_y):
#     queue = deque()
#     init_territory = territory[array[init_y][init_x]]
#     queue.append((init_x, init_y, init_territory[1]))
#     union_territory = init_territory[:]
#     while queue:
#         x, y, population = queue.popleft()
#         for dx, dy in DXY:
#             nx, ny = x + dx, y + dy
#             if nx < 0 or nx >= len(array[0]) or ny < 0 or ny >= len(array):
#                 continue
#
#             if check[ny][nx]:
#                 continue
#
#             if territory[array[ny][nx]] is territory[array[y][x]]:
#                 continue
#
#             population_diff = abs(population - territory[array[ny][nx]][1])
#             if population_diff < lower or population_diff > upper:
#                 continue
#
#             check[ny][nx] = True
#             new_territory = territory[array[ny][nx]]
#             territory[array[ny][nx]] = init_territory
#             union_territory[0] += new_territory[0]
#             union_territory[1] += new_territory[1]
#             queue.append((nx, ny, new_territory[1]))
#     if union_territory == init_territory:
#         return False
#     union_territory[1] = union_territory[1] // union_territory[0]
#     init_territory[0] = union_territory[0]
#     init_territory[1] = union_territory[1]
#     return True
#
#
# def check_union(array, territory, lower, upper):
#     check = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
#     continue_check = False
#     for y in range(len(array)):
#         for x in range(len(array[0])):
#             check[y][x] = True
#             if make_union(array, territory, check, lower, upper, x, y):
#                 continue_check = True
#     return continue_check
#
#
# def solution(array, territory, lower, upper):
#     # ToDo nomore 두기
#     day = 0
#     while True:
#         if not check_union(array, territory, lower, upper):
#             break
#         day += 1
#     return day
#
#
# # 1. 연합은 한 번 만들어지면 연결됨
# # -> 따라서 한 번 연결되면 경계선만 확인하면 됨
# # -> 더 이상 확인하지 않을 부분을 만들어서 True, False로 둠
# # 2. 연합은 동일성 비교로 확인
# # -> 연합을 넣을 때, 연합을 만들려는 값이랑 같은지 확인하는 부분이 필요
# if __name__ == '__main__':
#     array_num, lower, upper = (int(x) for x in read().split())
#     array = []
#     territory = []
#     for row_index in range(array_num):
#         column = []
#         for column_index, territory_info in enumerate([[1, int(x)] for x in read().split()]):
#             column.append(row_index * array_num + column_index)
#             territory.append(territory_info)
#         array.append(column)
#     print(solution(array, territory, lower, upper))
