# https://www.acmicpc.net/problem/11723
# Solved Date: 20.04.18.

import sys
read = sys.stdin.readline


class pythonic_set(set):
    def remove(self, element):
        if element in self:
            super().remove(element)

    def check(self, element):
        if element in self:
            return 1
        else:
            return 0

    def toggle(self, element):
        if element in self:
            self.remove(element)
        else:
            self.add(element)

    def all(self):
        for number in range(1, 21):
            self.add(number)

    def empty(self):
        self.clear()


class bitmask_set():
    def __init__(self):
        self.save = 0

    def add(self, element):
        self.save |= (1 << element - 1)

    def remove(self, element):
        self.save &= ~(1 << element - 1)

    def check(self, element):
        if self.save & (1 << element - 1):
            return 1
        else:
            return 0

    def toggle(self, element):
        self.save ^= (1 << element - 1)

    def all(self):
        self.save = (1 << 20) - 1

    def empty(self):
        self.save = 0


def main(mode=''):
    op_num = int(read().strip())
    if mode == 'bitmask':
        test_set = bitmask_set()
    else:
        test_set = pythonic_set()
    for _ in range(op_num):
        op = read().split()
        if op[0] == 'add':
            test_set.add(int(op[1]))
        elif op[0] == 'remove':
            test_set.remove(int(op[1]))
        elif op[0] == 'check':
            print(test_set.check(int(op[1])))
        elif op[0] == 'toggle':
            test_set.toggle(int(op[1]))
        elif op[0] == 'all':
            test_set.all()
        elif op[0] == 'empty':
            test_set.empty()


if __name__ == '__main__':
    main('bitmask')
