# https://www.acmicpc.net/problem/14502
# Solved Date: 20.05.19.

import sys
import collections
import itertools

read = sys.stdin.readline
DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))


def find_safety_area(board, visit):
    # 전체 확인하여 count하는 것이였으나, 느려서 뺌
    count = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if not visit[y][x] and board[y][x] == 0:
                count += 1
    return count


def make_wall(board, virus_pos, empty_pos, num, wall_pos=None, count=0, index=0):
    # 재귀 테스트 combination을 쓰는 것과 속도가 같음
    if wall_pos is None:
        wall_pos = []
    if count == num:
        return simulation_start(board, virus_pos, wall_pos)
    max_safety_area = 0
    for i in range(index, len(empty_pos)):
        wall_pos.append(empty_pos[i])
        safety_area = make_wall(board, virus_pos, empty_pos, num, wall_pos, count+1, i+1)
        if safety_area > max_safety_area:
            max_safety_area = safety_area
        wall_pos.pop()
    return max_safety_area


def simulation_start(board, virus_pos, wall_pos, empty_room_num):
    visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for y, x in wall_pos:
        visit[y][x] = True
    queue = collections.deque()
    for y, x in virus_pos:
        visit[y][x] = True
        queue.append((y, x))
    virus_room = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if new_y < 0 or new_y >= len(board) or new_x < 0 or new_x >= len(board[0]) or visit[new_y][new_x]:
                continue
            visit[new_y][new_x] = True
            if board[new_y][new_x] == 0:
                virus_room += 1
                queue.append((new_y, new_x))
    # https://www.acmicpc.net/source/12498412 참고
    return empty_room_num - len(wall_pos) - virus_room


def find_pos(board):
    virus_pos = []
    empty_pos = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                empty_pos.append((y, x))
            elif board[y][x] == 2:
                virus_pos.append((y, x))
    return virus_pos, empty_pos


def simulation_process(board):
    virus_pos, empty_pos = find_pos(board)
    max_safety_area = 0
    for wall_pos in itertools.combinations(empty_pos, 3):
        safety_area = simulation_start(board, virus_pos, wall_pos, len(empty_pos))
        if safety_area > max_safety_area:
            max_safety_area = safety_area
    return max_safety_area


def main():
    row, column = (int(x) for x in read().split())
    board = [[int(x) for x in read().split()] for _ in range(row)]
    print(simulation_process(board))


if __name__ == '__main__':
    main()
