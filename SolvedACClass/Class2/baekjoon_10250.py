# https://www.acmicpc.net/problem/10250
# Solved Date: 20.04.06.

import sys
read = sys.stdin.readline


def main():
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        height, width, num = (int(x) for x in read().split())
        floor = (num - 1) % height + 1
        if num == 1:
            dist = 1
        else:
            dist = (num - 1) // height + 1
        print("{}{:02}".format(floor, dist))


if __name__ == '__main__':
    main()
