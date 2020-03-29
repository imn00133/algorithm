# https://www.acmicpc.net/problem/1406
# https://www.acmicpc.net/source/18289071 - 출력속도를 높이기 위해 참고

import sys
read = sys.stdin.readline


def string_print(left_stack, right_stack):
	for _ in range(len(left_stack)):
		right_stack.append(left_stack.pop())
	for _ in range(len(right_stack)):
		print(right_stack.pop(), end='')


def edit(left_stack, right_stack, op):
	if op[0] == 'L':
		if left_stack:
			right_stack.append(left_stack.pop())
	elif op[0] == 'D':
		if right_stack:
			left_stack.append(right_stack.pop())
	elif op[0] == 'B':
		if left_stack:
			left_stack.pop()
	elif op[0] == 'P':
		left_stack.append(op[1])


def main():
	left_stack = list(read().strip())
	right_stack = []
	exec_num = int(read().strip())
	for _ in range(exec_num):
		op = read().split()
		edit(left_stack, right_stack, op)
	# string_print(left_stack, right_stack)
	print(''.join(left_stack + list(reversed(right_stack))))


def file_main():
	file = open('baekjoon_1406_input1.txt', mode='r', encoding='utf-8')
	left_stack = list(file.readline().strip())
	right_stack = []
	exec_num = int(file.readline().strip())
	for _ in range(exec_num):
		op = file.readline().split()
		edit(left_stack, right_stack, op)
	# string_print(left_stack, right_stack)
	print(''.join(left_stack + list(reversed(right_stack))))
	file.close()


if __name__ == '__main__':
	main()
