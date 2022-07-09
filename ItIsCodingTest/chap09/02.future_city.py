# 09 최단 경로 - 미래 도시
# Solved Date: 22.07.09.
import sys

read = sys.stdin.readline
INT = int(1e9)


def init(path_num, arr):
    for i in range(len(arr)):
        arr[i][i] = 0

    for _ in range(path_num):
        y, x = (int(x) for x in read().split())
        arr[y][x] = 1
        arr[x][y] = 1

    return arr


def fluid(arr):
    for k in range(1, len(arr)):
        for a in range(1, len(arr)):
            for b in range(1, len(arr)):
                arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
    return arr


def main():
    company_num, path_num = (int(x) for x in read().split())
    arr = [[INT for _ in range(company_num+1)] for _ in range(company_num+1)]
    arr = init(path_num, arr)
    arr = fluid(arr)

    x, k = (int(x) for x in read().split())
    if arr[1][k] == INT or arr[k][x] == INT:
        return -1
    return arr[1][k] + arr[k][x]


if __name__ == '__main__':
    print(main())
