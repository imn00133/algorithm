# https://leetcode.com/problems/lru-cache/
# Solved Date: 20.04.25.
import collections


class LRUCacheOrder(collections.OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key, last=True)
            return super().get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key, last=True)
        else:
            self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.next_del_queue = collections.deque()

    def get(self, key: int) -> int:
        if key in self.store:
            self.use(key)
            return self.store[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key][0] = value
            self.use(key)
        elif len(self.store) < self.capacity:
            self.new(key, value)
        else:
            while True:
                key_del = self.next_del_queue.popleft()
                if self.store[key_del][1]:
                    self.store[key_del][1] -= 1
                    continue
                else:
                    del(self.store[key_del])
                    self.new(key, value)
                    break

    def use(self, key: int) -> None:
        self.store[key][1] += 1
        self.next_del_queue.append(key)

    def new(self, key: int, value: int) -> None:
        temp = [value, 0]
        self.store[key] = temp
        self.next_del_queue.append(key)


def main():
    cache = LRUCacheOrder(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


if __name__ == '__main__':
    main()
