# https://www.acmicpc.net/problem/16964
# Solved Date: 20.04.25.

import sys

read = sys.stdin.readline


def validation_check(tree, ans):
    check = [False for _ in range(len(tree))]
    stack = []
    ans_index = 0
    node = ans[ans_index]
    # 처음이 1이 아니면 무조건 틀린다.
    if node != 1:
        return 0
    check[node] = True
    stack.append(node)
    while stack:
        node = stack.pop()
        next_node = ans[ans_index + 1]
        # node의 간선에 next_node가 없으면 pop을 버리고 이전으로
        if next_node not in tree[node]:
            continue
        check[next_node] = True
        ans_index += 1
        # ans를 다 확인하였으면 종료
        if ans_index == len(ans) - 1:
            return 1
        stack.append(node)
        stack.append(next_node)
    # 다 확인하지 못했으면 오류가 있다.
    # 이를 check[1:]로 하든, 아니든 0.04ms밖에 차이가 나지 않는다.
    # O(n)이 더 추가되었는데 흐음..?
    return 0


def main():
    vertex = int(read().strip())
    tree = [[] for _ in range(vertex + 1)]
    for _ in range(vertex - 1):
        node, con_node = (int(x) for x in read().split())
        tree[node].append(con_node)
        tree[con_node].append(node)
    ans = [int(x) for x in read().split()]
    print(validation_check(tree, ans))


if __name__ == '__main__':
    main()
