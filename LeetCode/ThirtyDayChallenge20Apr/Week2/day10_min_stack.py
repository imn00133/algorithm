# https://leetcode.com/problems/min-stack
# Solved Date: 20.04.10.


class FastMinStack(list):
    def __init__(self):
        super().__init__()
        self.min_num = []

    def push(self, x: int) -> None:
        self.append(x)
        if not self.min_num or x < self[self.min_num[-1]]:
            self.min_num.append(len(self) - 1)

    def pop(self, index=-1) -> None:
        if self:
            temp = super().pop()
            if self.min_num[-1] == len(self):
                temp = self.min_num.pop()

    def top(self) -> int:
        if self:
            return self[-1]

    def getMin(self) -> int:
        if self.min_num:
            return self[self.min_num[-1]]


class MinStack(list):
    def __init__(self):
        super().__init__()
        self.min_num = None

    def push(self, x: int) -> None:
        self.append(x)
        if self.min_num is None or self.min_num > x:
            self.min_num = x

    def pop(self, index=-1) -> None:
        if self:
            temp = super().pop()
        if self:
            self.min_num = min(self)
        else:
            self.min_num = None

    def top(self) -> int:
        if self:
            return self[-1]

    def getMin(self) -> int:
        return self.min_num


def main():
    min_stack = FastMinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-1)
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.getMin())


if __name__ == '__main__':
    main()
