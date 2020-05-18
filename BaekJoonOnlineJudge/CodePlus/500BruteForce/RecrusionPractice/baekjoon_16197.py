# https://www.acmicpc.net/problem/16197
# Solved Date: 20.05.18.

import sys
read = sys.stdin.readline

DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))
MAX = 11


def is_in_board(board, pos):
    y, x = pos
    if 0 <= y < len(board) and 0 <= x < len(board[0]):
        return True
    else:
        return False


def recursion(board, prev_coin_pos, count=0):
    if count == 10:
        return MAX
    count += 1
    min_count = MAX
    for dy, dx in DYX:
        new_coin_pos = []
        for y, x in prev_coin_pos:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]) and board[new_y][new_x] == '#':
                new_y, new_x = y, x
            new_coin_pos.append((new_y, new_x))
        # 이동이 이전과 같으면 더 이상 진행 안함
        if prev_coin_pos == new_coin_pos:
            continue
        # 코인이 겹치면 더 이상 진행 안함
        if new_coin_pos[0] == new_coin_pos[1]:
            continue

        coin0_check = is_in_board(board, new_coin_pos[0])
        coin1_check = is_in_board(board, new_coin_pos[1])
        if coin0_check and coin1_check:
            temp_count = recursion(board, new_coin_pos, count)
            if temp_count < min_count:
                min_count = temp_count
        # 한 번 나타나면 하위는 확인할 필요가 없다.
        elif coin0_check ^ coin1_check:
            min_count = count
            break
    return min_count


def find_coin(board):
    coin_pos = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 'o':
                coin_pos.append((y, x))
                if len(coin_pos) == 2:
                    return coin_pos


def main(mode=''):
    row, column = (int(x) for x in read().split())
    board = [list(read().strip()) for _ in range(row)]
    coin_pos = find_coin(board)
    count = recursion(board, coin_pos)
    if count <= 10:
        print(count)
    else:
        print(-1)


if __name__ == '__main__':
    main()
