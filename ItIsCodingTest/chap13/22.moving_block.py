# 13 DSP/BFS문제 - 감시 피하기
# Solved Date: 22.04.08.
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


# 전부 1을 두르면 충돌만 판단
def new_board(board):
    n_board = [[1 for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
    for y in range(len(board)):
        for x in range(len(board[0])):
            n_board[y+1][x+1] = board[y][x]
    return n_board


def solution(board):
    end_condition = (len(board[0]), len(board))
    board = new_board(board)
    time_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    queue = deque()
    queue.append(((1, 1), (2, 1), 0))
    while queue:
        left, right, past_second = queue.popleft()
        if left == end_condition or right == end_condition:
            return past_second

        second = past_second + 1
        for dx, dy in DXY:
            x, y = left
            nx, ny = x + dx, y + dy
            if board[ny][nx]:
                continue

            if time_board[ny][nx] != 0 and second > time_board[ny][nx]:
                continue

            time_board[ny][nx] = second
            queue.append((left, (nx, ny), second))

        for dx, dy in DXY:
            x, y = right
            nx, ny = x + dx, y + dy
            if board[ny][nx]:
                continue

            if time_board[ny][nx] != 0 and second > time_board[ny][nx]:
                continue

            time_board[ny][nx] = second
            queue.append(((nx, ny), right, second))


if __name__ == '__main__':
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
    print(solution(board))
