# https://www.acmicpc.net/problem/17143
# Solved Date: 20.04.26.

import sys
read = sys.stdin.readline


class Shark:
    def __init__(self, row, column, speed, direction, size):
        self.row = row
        self.column = column
        self.direction = direction
        self.speed = speed
        self.size = size

    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.size > other.size:
            return True
        else:
            return False

    def position(self):
        return self.row, self.column

    def move(self, board_pos):
        """
        board_size에서 1을 뺀 만큼 인덱스가 움직인다.
        ex) column = 3
        0 4  2
        135 135
         2  0 4
        """
        if self.speed == 0:
            return None
        elif self.direction == 1:
            board_size = board_pos[0] - 1
            calc_pos = board_size - self.row + self.speed
            if (calc_pos // board_size) % 2 == 1:
                self.direction = 2
            if self.direction == 1:
                self.row = board_size - (calc_pos % board_size)
            else:
                self.row = calc_pos % board_size
        elif self.direction == 2:
            board_size = board_pos[0] - 1
            calc_pos = self.row + self.speed
            if (calc_pos // board_size) % 2 == 1:
                self.direction = 1
            if self.direction == 2:
                self.row = calc_pos % board_size
            else:
                self.row = board_size - (calc_pos % board_size)
        elif self.direction == 3:
            board_size = board_pos[1] - 1
            calc_pos = self.column + self.speed
            if (calc_pos // board_size) % 2 == 1:
                self.direction = 4
            if self.direction == 3:
                self.column = calc_pos % board_size
            else:
                self.column = board_size - (calc_pos % board_size)
        else:
            board_size = board_pos[1] - 1
            calc_pos = board_size - self.column + self.speed
            if (calc_pos // board_size) % 2 == 1:
                self.direction = 3
            if self.direction == 4:
                self.column = board_size - (calc_pos % board_size)
            else:
                self.column = calc_pos % board_size


def simulate(board, shark_dict):
    catch_shark_size = 0
    board_pos = (len(board), len(board[0]))
    for fisher in range(len(board[0])):
        for y in range(len(board)):
            if board[y][fisher]:
                shark_index = board[y][fisher]
                catch_shark_size += shark_dict[shark_index].size
                # dictionary에서 지우고, board에서 지움
                del(shark_dict[shark_index])
                board[y][fisher] = 0
                break
        # shark를 이동시킨다.
        for shark_index in shark_dict.keys():
            shark_pos = shark_dict[shark_index].position()
            board[shark_pos[0]][shark_pos[1]] = 0
            shark_dict[shark_index].move(board_pos)
        # shark를 board에 배치한다.
        remove_shark_index = []
        for shark_index in shark_dict.keys():
            shark_pos = shark_dict[shark_index].position()
            if board[shark_pos[0]][shark_pos[1]]:
                locate_shark_index = board[shark_pos[0]][shark_pos[1]]
                if shark_dict[shark_index] < shark_dict[locate_shark_index]:
                    remove_shark_index.append(shark_index)
                else:
                    remove_shark_index.append(locate_shark_index)
                    board[shark_pos[0]][shark_pos[1]] = shark_index
            else:
                board[shark_pos[0]][shark_pos[1]] = shark_index
        # 겹친 상어를 삭제한다.
        for shark_index in remove_shark_index:
            del(shark_dict[shark_index])
    return catch_shark_size


def main():
    row, column, shark_num = (int(x) for x in read().split())
    board = [[0 for _ in range(column)] for _ in range(row)]
    shark_dict = {}
    for index in range(1, shark_num + 1):
        meta_data = [int(x) for x in read().split()]
        meta_data[0] -= 1
        meta_data[1] -= 1
        board[meta_data[0]][meta_data[1]] = index
        shark_dict[index] = Shark(*meta_data)
    print(simulate(board, shark_dict))


if __name__ == '__main__':
    main()
