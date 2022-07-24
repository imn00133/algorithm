# 17 그래프 이론 - 어두운 길
# Solved Date: 22.07.24.
import sys

read = sys.stdin.readline


def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    parent_x = find_parents(parents, x)
    parent_y = find_parents(parents, y)
    if parent_x < parent_y:
        parents[parent_y] = parent_x
    else:
        parents[parent_x] = parent_y


def kruskal(parents, graph):
    total_cost = 0
    for x, y, cost in graph:
        if find_parents(parents, x) == find_parents(parents, y):
            continue
        total_cost += cost
        union(parents, x, y)
    return total_cost


def read_graph():
    n, m = (int(x) for x in read().split())
    total_cost = 0
    graph = []
    for _ in range(m):
        x, y, cost = (int(x) for x in read().split())
        total_cost += cost
        graph.append((x, y, cost))

    parents = [i for i in range(n)]
    return graph, parents, total_cost


def example():
    total_cost = 0
    n = 7
    example_value = [
        [0, 1, 7],
        [0, 3, 5],
        [1, 2, 8],
        [1, 3, 9],
        [1, 4, 7],
        [2, 4, 5],
        [3, 4, 15],
        [3, 5, 6],
        [4, 5, 8],
        [4, 6, 9],
        [5, 6, 11]
    ]
    graph = []

    for x, y, cost in example_value:
        total_cost += cost
        graph.append((x, y, cost))

    parents = [i for i in range(n)]
    return graph, parents, total_cost


def main():
    graph, parents, total_cost = example()

    graph.sort(key=lambda x: x[2])
    print(total_cost - kruskal(parents, graph))


if __name__ == '__main__':
    main()
