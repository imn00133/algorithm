# 13 DSP/BFS문제 - 감시 피하기
# Solved Date: 22.04.08.
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

DXY_PARALLEL = ((1, 0), (0, 1), (-1, 0), (0, -1))


def is_collision_wall(board, pos):
    return board[pos[1]][pos[0]] == 1


def is_collision_board(board, left, right):
    return is_collision_wall(board, left) or is_collision_wall(board, right)


def is_passed(time_board, pos, time):
    return time_board[pos[1]][pos[0]] > time


def is_passed_board(time_board, left, right, time):
    return is_passed(time_board, left, time) and is_passed(time_board, right, time)


def set_time_board_pos(time_board, pos, time):
    time_board[pos[1]][pos[0]] = time


def set_time_board(time_board, left, right, time):
    set_time_board_pos(time_board, left, time)
    set_time_board_pos(time_board, right, time)


def new_position(pos, dxy):
    return pos[0] + dxy[0], pos[1] + dxy[1]


# 전부 1을 두르면 충돌만 판단
def new_board(board):
    n_board = [[1 for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
    for y in range(len(board)):
        for x in range(len(board[0])):
            n_board[y+1][x+1] = board[y][x]
    return n_board


def solution(board):
    end_position = (len(board[0]), len(board))
    board = new_board(board)
    time_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    queue = deque()
    queue.append(((1, 1), (2, 1), 0))
    while queue:
        left, right, second = queue.popleft()
        current_second = second + 1
        if left == end_position or right == end_position:
            return second

        for dxy in DXY_PARALLEL:
            new_left, new_right = new_position(left, dxy), new_position(right, dxy)
            if is_collision_board(board, new_left, new_right):
                continue

            if is_passed_board(time_board, new_left, new_right, current_second):
                continue

            set_time_board(time_board, new_left, new_right, current_second)
            queue.append((new_left, new_right, current_second))

        # 빼서 바꾸면 상대 위치가 됨
        relative_pos = left[1] - right[1], left[0] - right[0]
        for _ in range(2):
            relative_pos = (-relative_pos[0], -relative_pos[1])
            new_left = new_position(left, relative_pos)
            new_right = new_position(right, relative_pos)

            # 평행이동했을 때 부딪히는지 확인
            if is_collision_board(board, new_left, new_right):
                continue

            if not is_passed_board(time_board, new_right, right, current_second):
                set_time_board(time_board, new_right, right, current_second)
                queue.append((new_right, right, current_second))

            if not is_passed_board(time_board, left, new_left, current_second):
                set_time_board(time_board, left, new_left, current_second)
                queue.append((left, new_left, current_second))


if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    print(solution(board))
