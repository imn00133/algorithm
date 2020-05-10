# https://www.acmicpc.net/problem/1285
# Solved Date: 20.05.10.
# https://www.acmicpc.net/source/18327076 참고

import sys
read = sys.stdin.readline


def brute_force(coin_board, length):
    answer = len(coin_board) ** 2
    for index in range(1 << len(coin_board)):
        board_count = 0
        for x in range(len(coin_board[0])):
            count = 0
            for y in range(len(coin_board)):
                letter = coin_board[y][x]
                if index & (1 << y):
                    letter = not letter
                if letter:
                    count += 1
            if count > length - count:
                board_count += length - count
            else:
                board_count += count
        if answer > board_count:
            answer = board_count
    return answer


def main():
    arr_num = int(read().strip())
    coin_board = [[x == 'T' for x in read().strip()] for _ in range(arr_num)]
    print(brute_force(coin_board, arr_num))


if __name__ == '__main__':
    main()
