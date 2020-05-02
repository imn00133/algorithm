# https://www.acmicpc.net/problem/10828
# Solving Date: 20.03.21.
# 참고
# https://wayhome25.github.io/cs/2017/04/18/cs-20/
# https://daimhada.tistory.com/105 -> 잘못되어 있음
# 시간초과가 남으로, sys.stdin.readline을 추가한다.
# 참고 https://www.acmicpc.net/board/view/44990
import sys
input = sys.stdin.readline


class Stack(list):
	push = list.append

	def pop(self, index=-1):
		if self:
			return super().pop(index)
		else:
			return -1

	def empty(self):
		if not self:
			return True
		else:
			return False

	def top(self):
		if not self:
			return -1
		else:
			return self[-1]


def main():
	test_case_num = int(input().strip())
	stack = Stack()
	for test_num in range(test_case_num):
		op = input().strip().split()
		code = op[0]
		if code == "push":
			stack.push(op[1])
		elif code == "pop":
			print(stack.pop())
		elif code == "size":
			print(len(stack))
		elif code == "empty":
			print(int(stack.empty()))
		elif code == "top":
			print(stack.top())


def file_main():
	file = open('baekjoon_10828_input.txt', mode='r', encoding='utf-8')
	test_case_num = int(file.readline().strip())
	stack = Stack()
	for test_num in range(test_case_num):
		op = file.readline().split()
		code = op[0]
		print(code)
		if code == "push":
			stack.push(op[1])
		elif code == "pop":
			print(stack.pop())
		elif code == "size":
			print(len(stack))
		elif code == "empty":
			print(int(stack.empty()))
		elif code == "top":
			print(stack.top())
	file.close()


if __name__ == "__main__":
	main()
