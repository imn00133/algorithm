#
# Solved Date: 20.04.28.

import collections


class FirstUnique:
    def __init__(self, nums):
        self.unique = None
        self.next_unique_queue = collections.deque()
        self.manage_unique = collections.defaultdict(int)
        for number in nums:
            self.manage_unique[number] += 1
            if self.manage_unique[number] == 1:
                self.next_unique_queue.append(number)
        self.find_next_unique()

    def show_first_unique(self) -> int:
        if self.unique is not None:
            return self.unique
        else:
            return -1

    def add(self, value) -> None:
        self.manage_unique[value] += 1
        if self.manage_unique[value] == 1:
            self.next_unique_queue.append(value)
        if value == self.show_first_unique() or self.show_first_unique() == -1:
            self.find_next_unique()

    def find_next_unique(self):
        while self.next_unique_queue:
            number = self.next_unique_queue.popleft()
            if self.manage_unique[number] == 1:
                self.unique = number
                break
        else:
            self.unique = None


def test():
    queue = FirstUnique([2, 3, 5])
    print(queue.show_first_unique())
    queue.add(5)
    print(queue.show_first_unique())
    queue.add(2)
    print(queue.show_first_unique())
    queue.add(3)
    print(queue.show_first_unique())
    print()
    queue = FirstUnique([7, 7, 7])
    print(queue.show_first_unique())
    queue.add(7)
    queue.add(3)
    queue.add(3)
    queue.add(7)
    queue.add(17)
    print(queue.show_first_unique())
    print()
    queue = FirstUnique([809])
    print(queue.show_first_unique())
    queue.add(809)
    print(queue.show_first_unique())


if __name__ == '__main__':
    test()
