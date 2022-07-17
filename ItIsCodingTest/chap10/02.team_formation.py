# 10 그래프 이론 - 팀 결성
# Solved Date: 22.07.17.
import sys

read = sys.stdin.readline


def find_parent(parent_table, x):
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]


def union(parent_table, a, b):
    parent_a = find_parent(parent_table, a)
    parent_b = find_parent(parent_table, b)
    if parent_a < parent_b:
        parent_table[b] = parent_a
    else:
        parent_table[a] = parent_b


def find_same_team(parent_table, a, b):
    team_a = find_parent(parent_table, a)
    team_b = find_parent(parent_table, b)
    if team_a == team_b:
        print("YES")
    else:
        print("NO")


def main():
    n, m = (int(x) for x in read().split())
    parent_table = [i for i in range(n)]
    for _ in range(m):
        op, a, b = (int(x) for x in read().split())
        if op == 0:
            union(parent_table, a-1, b-1)
        else:
            find_same_team(parent_table, a-1, b-1)


if __name__ == '__main__':
    main()
