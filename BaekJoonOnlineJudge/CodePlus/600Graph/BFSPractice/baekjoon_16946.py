# https://www.acmicpc.net/problem/16946
# Solved Date: 20.06.06.

import sys
import collections

read = sys.stdin.readline
DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))


def count_space(board, visit, count, y, x):
    space_num = len(count)
    count_num = 1
    queue = collections.deque()
    visit[y][x] = space_num
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for dy, dx in DYX:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]) or board[ny][nx] == 1 or visit[ny][nx] > -1:
                continue
            visit[ny][nx] = space_num
            count_num += 1
            queue.append((ny, nx))
    count.append(count_num % 10)


def return_around_space(board, visit, count, y, x):
    sum_count = 0
    check_space = []
    for dy, dx in DYX:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]) or board[ny][nx] == 1:
            continue
        if visit[ny][nx] == -1:
            count_space(board, visit, count, ny, nx)
        space_num = visit[ny][nx]
        if space_num in check_space:
            continue
        check_space.append(space_num)
        sum_count += count[space_num]
    return (sum_count + 1) % 10


def find_wall(board):
    ans = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    # -1 방문안함, 0이상 공간 index
    visit = [[-1 for _ in range(len(board[0]))] for _ in range(len(board))]
    count = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                ans[y][x] = return_around_space(board, visit, count, y, x)
    return ans


def main():
    row, column = (int(x) for x in read().split())
    board = [[int(x) for x in list(read().strip())] for _ in range(row)]
    ans = find_wall(board)
    for index in range(len(ans)):
        print(*ans[index], sep='')


if __name__ == '__main__':
    main()
