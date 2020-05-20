# https://www.acmicpc.net/problem/9328
# Solved Date: 20.04.24.

import sys
import collections

read = sys.stdin.readline
DYX = ((1, 0), (0, 1), (-1, 0), (0, -1))


def check(board, queue, document_count, keys, doors, y, x):
    # 값이 삭제되는 모든 부분이 queue에 저장되어야 한다.
    value = board[y][x]
    if value == '$':
        document_count += 1
        board[y][x] = 0
        queue.append((y, x))
    elif ord('a') <= ord(value) <= ord('z'):
        index = ord(value) - ord('a')
        # key가 있든 없든 True로 만들어도 상관 없다.
        keys[index] = True
        board[y][x] = 0
        queue.append((y, x))
        # 문 좌표가 있으면 전부 넣음
        if doors[index]:
            for new_y, new_x in doors[index]:
                board[new_y][new_x] = 0
                queue.append((new_y, new_x))
    elif ord('A') <= ord(value) <= ord('Z'):
        index = ord(value) - ord('A')
        # key가 이전에 있었으면, 이미 doors내의 좌표는 전부 입력되었다.
        if keys[index]:
            board[y][x] = 0
            queue.append((y, x))
        else:
            doors[index].append((y, x))
    return document_count


def border(board, queue, document_count, keys, doors, y, x):
    if board[y][x] == '.':
        board[y][x] = 0
        queue.append((y, x))
    elif board[y][x]:
        document_count = check(board, queue, document_count, keys, doors, y, x)
    return document_count


def border_check(board, queue, document_count, keys, doors):
    # 외각을 점검하여, 시작 위치를 확인한다.
    for y in range(len(board)):
        x = 0
        document_count = border(board, queue, document_count, keys, doors, y, x)
        x = len(board[0]) - 1
        document_count = border(board, queue, document_count, keys, doors, y, x)
    for x in range(len(board[0])):
        y = 0
        document_count = border(board, queue, document_count, keys, doors, y, x)
        y = len(board) - 1
        document_count = border(board, queue, document_count, keys, doors, y, x)
    return document_count


def rub(board, having_keys):
    document_count = 0
    # 가진 키를 넣어 둠
    keys = [False for _ in range(ord('z') - ord('a') + 1)]
    for temp_key in having_keys:
        keys[ord(temp_key) - ord('a')] = True
    doors = [[] for _ in range(ord('Z') - ord('A') + 1)]
    queue = collections.deque()
    document_count = border_check(board, queue, document_count, keys, doors)
    while queue:
        y, x = queue.popleft()
        for dy, dx in DYX:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]) and board[new_y][new_x]:
                if board[new_y][new_x] == '.':
                    board[new_y][new_x] = 0
                    queue.append((new_y, new_x))
                else:
                    document_count = check(board, queue, document_count, keys, doors, new_y, new_x)
    return document_count


def main():
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        row, column = (int(x) for x in read().split())
        board = []
        for _ in range(row):
            board.append(list(read().strip()))
        having_key = list(read().strip())
        if having_key[0] == '0':
            having_key = []
        print(rub(board, having_key))


if __name__ == '__main__':
    main()
