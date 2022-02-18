import sys
from collections import deque

read = sys.stdin.readline

DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_in_ice_frame(x, y, ice_frame):
    return 0 <= x < len(ice_frame[0]) and 0 <= y < len(ice_frame)


def dfs(x, y, ice_frame, check):
    check[y][x] = True
    for dx, dy in DIRECTION:
        nx, ny = x + dx, y + dy
        if not is_in_ice_frame(nx, ny, ice_frame):
            continue
        if check[ny][nx] or ice_frame[ny][nx] == '1':
            continue
        dfs(nx, ny, ice_frame, check)


def bfs(x, y, ice_frame, check):
    queue = deque()
    queue.append((x, y))
    check[y][x] = True
    while len(queue):
        x, y = queue.popleft()
        for dx, dy in DIRECTION:
            nx, ny = x + dx, y + dy
            if not is_in_ice_frame(nx, ny, ice_frame):
                continue
            if check[ny][nx] or ice_frame[ny][nx] == '1':
                continue
            check[ny][nx] = True
            queue.append((nx, ny))


def solve(ice_frame, solve_dfs=False):
    check = [[False for _ in range(len(ice_frame[0]))] for _ in range(len(ice_frame))]
    method = bfs
    if solve_dfs:
        method = dfs

    answer = 0
    for y in range(len(ice_frame)):
        for x in range(len(ice_frame[0])):
            if check[y][x]:
                continue
            if ice_frame[y][x] == '0':
                answer += 1
                method(x, y, ice_frame, check)
            else:
                check[y][x] = True

    return answer


if __name__ == '__main__':
    row, column = (int(x) for x in read().split())
    ice_frame = [read().rstrip() for _ in range(row)]
    # print(*ice_frame, sep='\n')
    print(solve(ice_frame, True))

