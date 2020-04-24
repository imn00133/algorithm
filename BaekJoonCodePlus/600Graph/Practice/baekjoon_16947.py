# https://www.acmicpc.net/problem/16947
# Solved Date: 20.04.24.

import sys
import collections

read = sys.stdin.readline


def arrange_loop(check, stack, start_node):
    # stack을 확인하여 순환선일 경우 check에 0, 아닐 경우 -2를 입력
    check_value = 0
    while stack:
        node, pre_node, index = stack.pop()
        check[node] = check_value
        if node == start_node:
            check_value = -2
    return check


def find_loop(subway_map, check):
    # dfs
    node = 1
    pre_node = index = 0
    stack = [(node, pre_node, index)]
    check[node] = 0
    while stack:
        node, pre_node, index = stack.pop()
        for next_index in range(index, len(subway_map[node])):
            next_node = subway_map[node][next_index]
            # -2는 탐색했으나 막힘, -1은 아직 탐색 안함, 0은 탐색중
            if next_node == pre_node or check[next_node] == -2:
                continue
            elif check[next_node] == -1:
                check[next_node] = 0
                stack.append((node, pre_node, next_index+1))
                stack.append((next_node, node, 0))
                break
            else:
                stack.append((node, pre_node, next_index+1))
                check = arrange_loop(check, stack, next_node)
                break
        else:
            # for문이 정상적으로 종료했을 때만 작동한다.
            # index를 더 이상 출력할 수 없을 때(즉 막다른 곳) -2를 넣는다.
            check[node] = -2
    return check


def step(subway_map, check):
    # bfs
    queue = collections.deque()
    inspect = [False for _ in range(len(subway_map))]
    # 순환선에서 시작하도록 0인 부분의 index를 넣는다.
    node = check.index(0)
    count = 1
    queue.append((node, count))
    inspect[node] = True
    while queue:
        node, count = queue.popleft()
        if check[node] != 0:
            count += 1
        for next_node in subway_map[node]:
            if not inspect[next_node]:
                if check[next_node] != 0:
                    check[next_node] = count
                queue.append((next_node, count))
                inspect[next_node] = True
    return check


def main():
    vertex_num = int(read().strip())
    subway_map = [[] for _ in range(vertex_num + 1)]
    for _ in range(vertex_num):
        node, con_node = (int(x) for x in read().split())
        subway_map[node].append(con_node)
        subway_map[con_node].append(node)
    check = [-1 for _ in range(len(subway_map))]
    check = find_loop(subway_map, check)
    check = step(subway_map, check)
    print(*check[1:], sep=' ')


if __name__ == '__main__':
    main()
