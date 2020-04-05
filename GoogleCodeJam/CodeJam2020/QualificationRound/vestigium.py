# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c
# Solved Date: 20.04.05.

import sys
read = sys.stdin.readline


def check_line_overlap(line):
    set_line = set(line)
    if len(set_line) == len(line):
        return False
    else:
        return True


def make_column_line(arr, x):
    line = []
    for y in range(len(arr)):
        line.append(arr[y][x])
    return line


def calc_trace(arr):
    trace_value = 0
    for i in range(len(arr)):
        trace_value += arr[i][i]
    return trace_value


def main():
    test_case_num = int(read().strip())
    for test_case in range(1, test_case_num+1):
        line_num = int(read().strip())
        arr = []
        # make array
        for _ in range(line_num):
            arr.append([int(x) for x in read().split()])
        # trace of matrix
        trace_num = calc_trace(arr)
        # row overlap
        row_overlap = 0
        for row in arr:
            if check_line_overlap(row):
                row_overlap += 1
        # column overlap
        column_overlap = 0
        for index in range(line_num):
            if check_line_overlap(make_column_line(arr, index)):
                column_overlap += 1
        # result
        print("Case #{}: {} {} {}".format(test_case, trace_num, row_overlap, column_overlap))


if __name__ == '__main__':
    main()
