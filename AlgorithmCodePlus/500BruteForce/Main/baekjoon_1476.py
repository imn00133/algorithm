# https://www.acmicpc.net/problem/1476
# Solved Date: 20.04.04.

import sys
read = sys.stdin.readline


def brute_force(years):
    max_years = (15, 28, 19)
    max_year = 1
    for value in max_years:
        max_year *= value
    jun_years = [0 for _ in range(len(max_years))]
    for earth_year in range(max_year + 1):
        if jun_years == years:
            return earth_year + 1
        for i in range(len(jun_years)):
            jun_years[i] = (jun_years[i] + 1) % max_years[i]


def main():
    years = [int(x) - 1 for x in read().split()]
    print(brute_force(years))


if __name__ == '__main__':
    main()
