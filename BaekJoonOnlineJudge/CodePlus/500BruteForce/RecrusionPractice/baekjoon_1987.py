# https://www.acmicpc.net/problem/1987
# Solved Date: 20.05.22.

import sys
read = sys.stdin.readline

DYX = ((-1, 0), (0, 1), (1, 0), (0, -1))


def recursion(board, check, y=0, x=0, count=1):
    if count == len(check):
        return count
    max_count = count
    for dy, dx in DYX:
        ny, nx = y + dy, x + dx
        if ny >= len(board) or ny < 0 or nx >= len(board[0]) or nx < 0:
            continue
        index = ord(board[ny][nx]) - ord('A')
        if check[index]:
            continue
        check[index] = True
        temp_count = recursion(board, check, ny, nx, count + 1)
        check[index] = False
        if temp_count > max_count:
            max_count = temp_count
    return max_count


def main():
    row, column = (int(x) for x in read().split())
    board = [read().strip() for _ in range(row)]
    check = [False for _ in range(ord('Z') - ord('A') + 1)]
    check[ord(board[0][0]) - ord('A')] = True
    print(recursion(board, check))


if __name__ == '__main__':
    main()
