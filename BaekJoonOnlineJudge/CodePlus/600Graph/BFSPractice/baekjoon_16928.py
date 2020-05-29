# https://www.acmicpc.net/problem/16928
# Solved Date: 20.05.29.

import sys
import collections
read = sys.stdin.readline

MAX_BOARD = 100
DICE_NUM = 6


def explorer(board):
    visit = [False for _ in range(len(board))]
    queue = collections.deque()
    # node, count
    visit[1] = True
    queue.append((1, 0))
    while queue:
        node, count = queue.popleft()
        for step in range(1, DICE_NUM + 1):
            new_step = node + step
            if new_step > 100 or visit[new_step]:
                continue
            if board[new_step]:
                new_step = board[new_step][0]
            # node에서 100을 넘기든, 여기서 넘기든 시간이 같다.
            if new_step == 100:
                return count + 1
            visit[new_step] = True
            queue.append((new_step, count + 1))


def main():
    board = [[] for _ in range(MAX_BOARD+1)]
    ladder, snake = (int(x) for x in read().split())
    for _ in range(ladder + snake):
        node, con_node = (int(x) for x in read().split())
        board[node].append(con_node)
    print(explorer(board))


if __name__ == '__main__':
    main()
