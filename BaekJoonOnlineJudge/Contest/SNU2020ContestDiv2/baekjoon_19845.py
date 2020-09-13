import sys

read = sys.stdin.readline


def binary_explorer(rows_nemmo, pos):
    x, y = pos
    start = y
    end = len(rows_nemmo)
    mid = (start + end) // 2
    while start < end:
        if rows_nemmo[mid] >= x:
            start = mid + 1
        else:
            end = mid
        mid = (start + end) // 2
    return start - y - 1


def cal(rows_nemmo, pos):
    x, y = pos
    die_nemmo = rows_nemmo[y] - x + 1
    if die_nemmo <= 0:
        return 0
    die_nemmo += binary_explorer(rows_nemmo, pos)
    return die_nemmo


def main():
    column_num, laser_num = (int(x) for x in read().split())
    rows_nemmo = [int(x) - 1 for x in read().split()]
    for _ in range(laser_num):
        pos = [int(x) - 1 for x in read().split()]
        print(cal(rows_nemmo, pos))


if __name__ == "__main__":
    main()
