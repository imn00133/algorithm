#
# Solved Date: 20.05.09.


def explorer(adj_node, keys, lock):
    visit = [False for _ in range(len(adj_node))]
    from collections import deque
    queue = deque()
    if lock[0]:
        return False
    if 0 in keys:
        lock[keys[0]] = False
    queue.append(0)
    visit[0] = True
    while queue:
        node = queue.popleft()
        for next_node in adj_node[node]:
            if visit[next_node]:
                continue
            if lock[next_node]:
                visit[next_node] = True
                continue
            queue.append(next_node)
            visit[next_node] = True
            if next_node in keys:
                door = keys[next_node]
                lock[door] = False
                if visit[door]:
                    queue.append(door)
    return all(visit)


def solution(n, path, order):
    adj_node = [[] for _ in range(n)]
    for node, con_node in path:
        adj_node[node].append(con_node)
        adj_node[con_node].append(node)
    lock = [False for _ in range(n)]
    keys = {}
    for key, door in order:
        keys[key] = door
        lock[door] = True
    return explorer(adj_node, keys, lock)
