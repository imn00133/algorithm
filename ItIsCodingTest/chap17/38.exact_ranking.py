# 17 최단 경로 - 정확한 순위
# Solved Date: 22.07.24.
import sys

read = sys.stdin.readline
INF = int(1e9)


def floyd(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


def calc_answer(arr):
    answer = 0
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i][j] != INF or arr[j][i] != INF:
                count += 1
        if count == len(arr):
            answer += 1
    return answer


def main():
    n, m = (int(x) for x in read().split())
    arr = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr[i][i] = 0

    for _ in range(m):
        x, y = (int(x) for x in read().split())
        arr[y-1][x-1] = 1

    floyd(arr)

    print(calc_answer(arr))


if __name__ == '__main__':
    main()
