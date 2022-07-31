# 17 그래프 이론 - 여행 계획
# Solved Date: 22.07.31.
import sys

read = sys.stdin.readline


def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]


def union(parents, a, b):
    parents_a = find_parent(parents, a)
    parents_b = find_parent(parents, b)
    if parents_a < parents_b:
        parents[b] = parents_a
    else:
        parents[a] = parents_b


# 서로소 집합을 확인하여 계획이 다른 서로소 집합에 있을 경우 여행이 불가능
def solution(graph, plan):
    parents = [i for i in range(len(graph))]
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[y][x]:
                union(parents, x, y)

    for i in range(len(plan)-1):
        if find_parent(parents, plan[i]) != find_parent(parents, plan[i+1]):
            return "NO"

    return "YES"


def main():
    n, m = (int(x) for x in read().split())
    graph = [[int(x) for x in read().split()] for _ in range(n)]
    plan = [int(x) for x in read().split()]
    print(solution(graph, plan))


if __name__ == '__main__':
    main()
