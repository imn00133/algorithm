# https://www.acmicpc.net/problem/16940
# Solved Date: 20.04.24.

import sys
import collections

read = sys.stdin.readline


def validation_check(tree, ans):
    # bfs
    queue = collections.deque()
    check = [False for _ in range(len(tree))]
    # ans = 답을 어디까지 확인했는지 기록하는 값이다.
    ans_index = 0
    node = ans[ans_index]
    # 시작이 1이 아니면 무조건 틀렸다.
    if node != 1:
        return 0
    queue.append(node)
    check[node] = True
    ans_index += 1
    # ans를 다 돌면 종료한다.
    while ans_index != len(ans):
        node = queue.popleft()
        candidate = []
        # queue에서 pop한 node의 연결리스트에서 후보가 될 수 있는 값을 뽑는다.
        for number in tree[node]:
            if not check[number]:
                candidate.append(number)
        # 순회하는 답은 candidate와 같은 길이여야 한다. 이 내에 없는 값이 있을 경우 틀린 것으로 처리한다.
        for index in range(ans_index, ans_index + len(candidate)):
            ans_num = ans[index]
            if ans_num in candidate:
                check[ans_num] = True
                queue.append(ans_num)
            else:
                return 0
        ans_index += len(candidate)
    return 1


def main():
    vertex_num = int(read().strip())
    tree = [[] for _ in range(vertex_num + 1)]
    for _ in range(vertex_num - 1):
        node, con_node = (int(x) for x in read().split())
        tree[node].append(con_node)
        tree[con_node].append(node)
    ans = [int(x) for x in read().split()]
    print(validation_check(tree, ans))


if __name__ == '__main__':
    main()
