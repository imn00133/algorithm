# https://www.acmicpc.net/problem/10866
# Solving Date: 20.03.24.
# https://excelsior-cjh.tistory.com/96 참고

import sys
from collections import deque
read = sys.stdin.readline


class Deque(deque):
    push_front = deque.appendleft
    push_back = deque.append

    def pop_front(self):
        if self:
            return self.popleft()
        else:
            return -1

    def pop_back(self):
        if self:
            return self.pop()
        else:
            return -1

    def empty(self):
        if self:
            return False
        else:
            return True

    def front(self):
        if self:
            return self[0]
        else:
            return -1

    def back(self):
        if self:
            return self[-1]
        else:
            return -1


def deque_ctrl(deque_ins, op):
    if op[0] == 'push_front':
        deque_ins.push_front(op[1])
    elif op[0] == 'push_back':
        deque_ins.push_back(op[1])
    elif op[0] == 'pop_front':
        print(deque_ins.pop_front())
    elif op[0] == 'pop_back':
        print(deque_ins.pop_back())
    elif op[0] == 'size':
        print(len(deque_ins))
    elif op[0] == 'empty':
        print(int(deque_ins.empty()))
    elif op[0] == 'front':
        print(deque_ins.front())
    elif op[0] == 'back':
        print(deque_ins.back())


def main():
    test_op_num = int(read().strip())
    deque_ins = Deque()
    for op_num in range(test_op_num):
        op = read().split()
        deque_ctrl(deque_ins, op)


def file_main():
    file = open('baekjoon_10866_input2.txt', mode='r', encoding='utf-8')
    test_op_num = int(file.readline().strip())
    deque_ins = Deque()
    for op_num in range(test_op_num):
        op = file.readline().split()
        deque_ctrl(deque_ins, op)
    file.close()


if __name__ == '__main__':
    main()
