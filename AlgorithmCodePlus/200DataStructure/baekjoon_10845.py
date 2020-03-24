# https://www.acmicpc.net/problem/10845
# 참고
# https://daimhada.tistory.com/107
# https://wayhome25.github.io/cs/2017/04/18/cs-21/
# 단, 이번 구현에서는 삭제하지 않고 구현하여, O(1)로 고정하였다. (메모리 누수 문제)
# 원형큐를 구현하는 방법도 있긴 한데...

import sys
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


def queue_control(queue, op):
	if op[0] == 'push':
		queue.push(op[1])
	elif op[0] == 'pop':
		print(queue.pop())
	elif op[0] == 'size':
		print(queue.size())
	elif op[0] == 'empty':
		print(int(queue.empty()))
	elif op[0] == 'front':
		print(queue.front())
	elif op[0] == 'back':
		print(queue.back())


def main():
	test_op_num = int(read().strip())
	queue = Queue()
	for op_num in range(test_op_num):
		op = read().split()
		queue_control(queue, op)


def file_main():
	file = open('baekjoon_10845_input.txt', mode='r', encoding='utf-8')
	test_op_num = int(file.readline().strip())
	queue = Queue()
	for op_num in range(test_op_num):
		op = file.readline().split()
		queue_control(queue, op)


if __name__ == '__main__':
	main()
