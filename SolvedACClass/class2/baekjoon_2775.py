# https://www.acmicpc.net/problem/2775
# Solved Date: 20.04.09.

import sys
read = sys.stdin.readline


def solved(k, n):
    people = [i for i in range(1, n+1)]
    for _ in range(k):
        # 1부터 시작하여 people[index] += people[index-1]로 변경할 수 있다.
        for index, person in enumerate(people):
            if index == 0:
                continue
            people[index] = people[index-1] + person
    return people[-1]


def main():
    test_case_num = int(read().strip())
    for _ in range(test_case_num):
        k = int(read().strip())
        n = int(read().strip())
        print(solved(k, n))


if __name__ == '__main__':
    main()
