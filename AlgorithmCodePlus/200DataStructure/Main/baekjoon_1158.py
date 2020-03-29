# https://www.acmicpc.net/problem/1158
# Solving Date: 20.03.24.
# 10845에서 작성한 queue사용
# 작성한 queue로는 시간초과가 발생하여, deque를 queue로 활용하여 해결함

import sys
from collections import deque
read = sys.stdin.readline


class Queue(list):
	push = list.append

	def __init__(self):
		super().__init__()
		self.front_ptr = 0

	def size(self):
		return len(self) - self.front_ptr

	def pop(self, index=-1):
		if self.size() >= 1:
			self.front_ptr += 1
			return self[self.front_ptr-1]
		else:
			return -1

	def empty(self):
		if self.size() >= 1:
			return False
		else:
			return True

	def front(self):
		if self.size() >= 1:
			return self[self.front_ptr]
		else:
			return -1

	def back(self):
		if self.size() >= 1:
			return self[-1]
		else:
			return -1


def queue_main():
	n, k = [int(x) for x in read().split()]
	queue = Queue()
	josephus_per = []
	for people in range(n):
		queue.push(people+1)
	while not queue.empty():
		for _ in range(k-1):
			queue.push(queue.pop())
		josephus_per.append(queue.pop())
	print(str(josephus_per).replace('[', '<').replace(']', '>'))


def deque_main():
	n, k = [int(x) for x in read().split()]
	queue = deque()
	josephus_per = []
	for people in range(n):
		queue.append(people+1)
	while queue:
		for _ in range(k-1):
			queue.append(queue.popleft())
		josephus_per.append(queue.popleft())
	print(str(josephus_per).replace('[', '<').replace(']', '>'))


if __name__ == '__main__':
	deque_main()
