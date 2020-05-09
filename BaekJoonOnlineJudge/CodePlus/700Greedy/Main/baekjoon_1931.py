# https://www.acmicpc.net/problem/1931
# Solved Date: 20.05.08.

import sys
import operator
read = sys.stdin.readline


class TimeTable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"start: {self.start}, end: {self.end}"

    def __repr__(self):
        return f"TimeTable({self.start}, {self.end})"


def find_conference(conferences):
    count = 0
    end_time = 0
    for current in conferences:
        if current.start >= end_time:
            count += 1
            end_time = current.end
    return count


def fast_find_conference(conferences):
    count = 0
    start_time = conferences[-1][1]
    for current in reversed(conferences):
        if current[1] <= start_time:
            count += 1
            start_time = current[0]
    return count


def main(mode=''):
    conference_num = int(read().strip())
    conferences = []
    if mode == 'slow':
        for _ in range(conference_num):
            conferences.append(TimeTable(*(int(x) for x in read().split())))
        conferences.sort(key=operator.attrgetter('end', 'start'))
        print(find_conference(conferences))
    else:
        # https://www.acmicpc.net/source/14936101 참고
        for _ in range(conference_num):
            conferences.append(tuple((int(x) for x in read().split())))
        conferences.sort()
        print(fast_find_conference(conferences))


if __name__ == '__main__':
    main()
