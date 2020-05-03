# https://www.acmicpc.net/problem/1967
# Solved Date: 20.05.03.

import sys
import collections
sys.setrecursionlimit(10 ** 6)

read = sys.stdin.readline


def post_order(adj_node, check, node=1):
    if not adj_node[node]:
        return 0, 0
    weights = []
    max_weight = 0
    for next_node, next_weight in adj_node[node]:
        if not check[next_node]:
            check[next_node] = True
            sub_weight, sub_max_weight = post_order(adj_node, check, next_node)
            weights.append(next_weight + sub_weight)
            max_weight = max(sub_max_weight, max_weight)
    if len(weights) == 1:
        return weights[0], max_weight
    else:
        weights.sort(reverse=True)
        return weights[0], max(max_weight, weights[0] + weights[1])


def explore_tree(adj_node, root=1):
    check = [False for _ in range(len(adj_node))]
    queue = collections.deque()
    check[root] = True
    # node, weight
    queue.append((root, 0))
    max_node = max_weight = 0
    while queue:
        node, weight = queue.popleft()
        for next_node, next_weight in adj_node[node]:
            if not check[next_node]:
                check[next_node] = True
                total_weight = weight + next_weight
                queue.append((next_node, total_weight))
                if max_weight < total_weight:
                    max_node = next_node
                    max_weight = total_weight
    return max_node, max_weight


def main(mode=''):
    node_num = int(read().strip())
    adj_node = [[] for _ in range(node_num + 1)]
    for _ in range(node_num - 1):
        node, con_node, weight = (int(x) for x in read().split())
        adj_node[node].append((con_node, weight))
        if mode != 'dfs':
            adj_node[con_node].append((node, weight))
    if mode == 'dfs':
        check = [False for _ in range(len(adj_node))]
        max_weight = max(post_order(adj_node, check))
    else:
        start_node, _ = explore_tree(adj_node)
        _, max_weight = explore_tree(adj_node, start_node)
    print(max_weight)


if __name__ == '__main__':
    main()
