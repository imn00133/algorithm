# https://leetcode.com/problems/number-of-islands/
# Solved Date: 20.04.18.


def num_islands(grid):
    def new_island_explore(row, col, max_row, max_col):
        if not(-1 < row < max_row and -1 < col < max_col):
            return 0
        if grid[row][col] == '1':
            grid[row][col] = '0'
            new_island_explore(row, col+1, max_row, max_col)
            new_island_explore(row+1, col, max_row, max_col)
            new_island_explore(row-1, col, max_row, max_col)
            new_island_explore(row, col-1, max_row, max_col)
        else:
            return 0
        return 0

    island_count = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == '1':
                island_count += 1
                new_island_explore(j, i, len(grid), len(grid[0]))
    return island_count


def main():
    row_num = int(input())
    grid = []
    for _ in range(row_num):
        grid.append(list(input()))
    print(num_islands(grid))


if __name__ == '__main__':
    main()
