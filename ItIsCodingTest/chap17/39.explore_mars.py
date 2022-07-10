# 17 최단 경로 - 화성탐사
# Solved Date: 22.07.10.
import sys
import heapq
from collections import deque

read = sys.stdin.readline
INF = int(1e9)
DXY = ((1, 0), (0, 1), (-1, 0), (0, -1))


def make_arr():
    arr_size = int(read().rstrip())
    arr = []
    for _ in range(arr_size):
        arr.append([int(x) for x in read().split()])
    return arr


def bfs(arr):
    cost_table = [[INF for _ in range(len(arr))] for _ in range(len(arr))]

    init_x, init_y = 0, 0
    current_cost = arr[init_y][init_x]
    cost_table[init_y][init_x] = current_cost

    queue = deque()
    queue.append((init_x, init_y, current_cost))
    while queue:
        x, y, cost = queue.popleft()
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(arr[0]) or ny < 0 or ny >= len(arr):
                continue

            next_cost = cost + arr[ny][nx]
            if next_cost > cost_table[ny][nx]:
                continue

            cost_table[ny][nx] = next_cost
            queue.append((nx, ny, next_cost))

    return cost_table[-1][-1]


def dijkstra(arr):
    cost_table = [[INF for _ in range(len(arr))] for _ in range(len(arr))]
    pq = []

    init_x, init_y = 0, 0
    cost = arr[init_y][init_x]
    cost_table[init_y][init_x] = cost
    heapq.heappush(pq, (cost, init_x, init_y))

    while pq:
        cost, x, y = heapq.heappop(pq)
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(arr[0]) or ny < 0 or ny >= len(arr):
                continue

            next_cost = cost + arr[ny][nx]
            if next_cost > cost_table[ny][nx]:
                continue

            cost_table[ny][nx] = next_cost
            heapq.heappush(pq, (next_cost, nx, ny))

    return cost_table[-1][-1]


def main(function):
    test_num = int(read().rstrip())
    for _ in range(test_num):
        arr = make_arr()
        print(function(arr))


def test_main(function):
    test_1 = [[5, 5, 4],
              [3, 9, 1],
              [3, 2, 7]]
    print(function(test_1))

    test_2 = [[3, 7, 2, 0, 1],
              [2, 8, 0, 9, 1],
              [1, 2, 1, 8, 1],
              [9, 8, 9, 2, 0],
              [3, 6, 5, 1, 5]]
    print(function(test_2))

    test_3 = [[9, 0, 5, 1, 1, 5, 3],
              [4, 1, 2, 1, 6, 5, 3],
              [0, 7, 6, 1, 6, 8, 5],
              [1, 1, 7, 8, 3, 2, 3],
              [9, 4, 0, 7, 6, 4, 1],
              [5, 8, 3, 2, 4, 8, 3],
              [7, 4, 8, 4, 8, 3, 4]]
    print(function(test_3))


if __name__ == '__main__':
    test_main(dijkstra)
