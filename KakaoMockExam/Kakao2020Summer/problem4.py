#
# Solved Date: 20.05.09.

DYX = ((0, 1), (-1, 0), (0, -1), (1, 0))


def explorer(board):
    from collections import deque
    board[0][0] = 1
    queue = deque()
    if board[0][1] == 0:
        board[0][1] = 100
        queue.append((0, 1, 100, 0))
    if board[1][0] == 0:
        board[1][0] = 100
        queue.append((1, 0, 100, 3))
    # y, x, 총 가격, direction(오른쪽: 0, 위쪽: 1, 왼쪽: 2, 아래쪽: 3)
    while queue:
        y, x, current_value, direction = queue.popleft()
        for index in range(len(DYX)):
            if abs(direction - index) == 2:
                continue
            new_y, new_x = y + DYX[index][0], x + DYX[index][1]
            if direction == index:
                next_value = current_value + 100
            else:
                next_value = current_value + 600
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]) and board[new_y][new_x] != 1:
                if board[new_y][new_x] == 0 or next_value <= board[new_y][new_x]:
                    board[new_y][new_x] = next_value
                    queue.append((new_y, new_x, next_value, index))
    return board[-1][-1]


def solution(board):
    answer = explorer(board)
    return answer


def main():
    board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(board))


if __name__ == '__main__':
    main()
