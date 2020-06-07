# https://www.acmicpc.net/problem/16236
# Solved Date: 20.06.07.

import sys
import collections

read = sys.stdin.readline
# 위쪽, 왼쪽, 오른쪽, 아래를 점검하여 위쪽과 왼쪽을 먼저 확인하도록 한다.
DYX = ((-1, 0), (0, -1), (0, 1), (1, 0))


class BabyShark:
    def __init__(self, y, x, size=2):
        self.pos = (y, x)
        self.size = size
        self.eaten = 0

    def __str__(self):
        return f"pos: {self.pos}, size: {self.size}"

    def __repr__(self):
        return f"BabyShark({self.pos[0]}, {self.pos[1]}, {self.size}"

    def find_food(self, board):
        # 먹이를 찾으면 시간을 반환, 못찾으면 0을 반환
        fish_pos = self._explorer(board)
        if not fish_pos:
            return 0
        fish_pos.sort()
        y, x, count = fish_pos[0]
        self._eat_food(board, y, x)
        return count

    def _explorer(self, board):
        visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        queue = collections.deque()
        y, x = self.pos
        visit[y][x] = True
        # y, x, 0
        queue.append((y, x, 0))
        fish_pos = []
        find_count = 0
        while queue:
            y, x, count = queue.popleft()
            count += 1
            for dy, dx in DYX:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]) or visit[ny][nx]:
                    continue
                visit[ny][nx] = True
                site = board[ny][nx]
                if site == 0 or site == self.size:
                    queue.append((ny, nx, count))
                elif board[ny][nx] < self.size:
                    if fish_pos and find_count != count:
                        queue.clear()
                    else:
                        find_count = count
                        fish_pos.append((ny, nx, count))
        return fish_pos

    def _eat_food(self, board, y, x):
        self.eaten += 1
        if self.size == self.eaten:
            self.eaten = 0
            self.size += 1
        self.pos = (y, x)
        board[y][x] = 0


def simulation(board, baby_shark):
    count = 0
    while True:
        next_count = baby_shark.find_food(board)
        if next_count == 0:
            return count
        count += next_count


def find_shark(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 9:
                board[y][x] = 0
                baby_shark = BabyShark(y, x)
                return baby_shark


def main():
    board_num = int(read().strip())
    board = [[int(x) for x in read().split()] for _ in range(board_num)]
    baby_shark = find_shark(board)
    print(simulation(board, baby_shark))


if __name__ == '__main__':
    main()
