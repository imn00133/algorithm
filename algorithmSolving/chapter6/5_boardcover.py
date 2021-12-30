# Solving Date: 20.01.02.
# site: https://algospot.com/judge/problem/read/BOARDCOVER

# 주어진 칸을 덮는 네 가지 방법
# COVERTYPE: 블럭을 구성하는 세 칸의 상대적 위치 (dy, dx)의 목록
COVERTYPE = (
    ((0, 0), (1, 0), (0, 1)),
    ((0, 0), (0, 1), (1, 1)),
    ((0, 0), (1, 0), (1, 1)),
    ((0, 0), (1, 0), (1, -1))
)


def set_cover(board, y, x, cover_type, delta):
    # covertype방법으로 덮거나 뺀다
    # delta가 1이면 덮고, -1이면 뺀다.
    # 덮은 블록에 문제(넘어가거나, 겹치거나 다시 덮을 때)가 있으면 False반환
    check = True
    for i in range(3):
        ny = y + COVERTYPE[cover_type][i][0]
        nx = x + COVERTYPE[cover_type][i][1]
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            check = False
        else:
            board[ny][nx] += delta
            if board[ny][nx] > 1:
                check = False
    return check


def cover(board):
    x, y = -1, -1
    # y, x보다는 x, y로 계산하는게 편해서 바꾸려고 했는데 더 어렵다.
    # 보통 행, 열로 계산을 하는데, 행은 y값의 변화고, 열은 x값의 변화로 보는게 편하다.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break
    # 기저 사례: 모든 칸을 채웠으면 1을 반환
    if y == -1:
        return 1
    ret = 0
    for cover_type in range(4):
        if set_cover(board, y, x, cover_type, 1):
            ret += cover(board)
        set_cover(board, y, x, cover_type, -1)
    # 반환값 까먹지 말자. 자꾸 None type을 더한다고 빼액 했는데... 결론은 반환값 빼먹음
    return ret


def main():
    case_num = int(input())
    for _ in range(case_num):
        height, width = tuple(map(int, input().split()))
        board = []
        for _ in range(height):
            temp_line = ' '.join(input()).split()
            for i in range(width):
                if temp_line[i] == '#':
                    temp_line[i] = 1
                else:
                    temp_line[i] = 0
            board.append(temp_line)
        print(cover(board))


def file_main():
    file = open('5_test.txt', 'r', encoding='utf-8')
    case_num = int(file.readline())
    for _ in range(case_num):
        height, width = tuple(map(int, file.readline().split()))
        board = []
        for _ in range(height):
            temp_line = ' '.join(file.readline()).split()
            for i in range(width):
                if temp_line[i] == '#':
                    temp_line[i] = 1
                else:
                    temp_line[i] = 0
            board.append(temp_line)
        print(cover(board))
    file.close()


if __name__ == '__main__':
    main()
