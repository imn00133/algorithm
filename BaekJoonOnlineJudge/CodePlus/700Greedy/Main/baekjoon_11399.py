# https://www.acmicpc.net/problem/11399
# Solved Date: 20.05.09.

import sys
read = sys.stdin.readline


def main():
    arr_num = read().strip()
    times = [int(x) for x in read().split()]
    times.sort()
    cumulative_sum_time = [times[0]]
    for index in range(1, len(times)):
        cumulative_sum_time.append(cumulative_sum_time[index-1] + times[index])
    print(sum(cumulative_sum_time))


if __name__ == '__main__':
    main()
