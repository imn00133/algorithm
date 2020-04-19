#
# Solved Date: 20.04.19.


def slow_path_sum(grid):
    row = len(grid)
    col = len(grid[0])
    for y in range(row):
        for x in range(col):
            path_temp = 0
            if x > 0 and y > 0:
                col_temp = grid[y][x - 1]
                row_temp = grid[y - 1][x]
                path_temp = min(col_temp, row_temp)
            elif x > 0:
                path_temp = grid[y][x - 1]
            elif y > 0:
                path_temp = grid[y - 1][x]
            grid[y][x] += path_temp
    return grid[-1][-1]


def min_path_sum(grid):
    row = len(grid)
    col = len(grid[0])
    for y in range(row):
        for x in range(col):
            if x == 0 and y == 0:
                continue
            if x < 1:
                path_temp = grid[y-1][x]
            elif y < 1:
                path_temp = grid[y][x-1]
            else:
                col_temp = grid[y][x-1]
                row_temp = grid[y-1][x]
                path_temp = min(col_temp, row_temp)
            grid[y][x] += path_temp
    return grid[-1][-1]


def main():
    arr_num = int(input())
    grid = []
    for _ in range(arr_num):
        grid.append([int(x) for x in input().split()])
    print(min_path_sum(grid))


if __name__ == '__main__':
    main()
