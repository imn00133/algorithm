# https://www.acmicpc.net/problem/1874
# Solving Date: 20.03.21.
# op_str을 string으로 처리하여 +=, -=를 사용할 경우 8배 정도 시간이 더 걸린다.

import sys
read = sys.stdin.readline


def stack_op(num_in, stack, next_push, op_str):
	if not stack:
		stack.append(next_push)
		op_str.append('+')
		next_push += 1
	if num_in >= stack[-1]:
		while num_in != stack[-1]:
			stack.append(next_push)
			op_str.append('+')
			next_push += 1
		stack.pop()
		op_str.append('-')
	else:
		op_str = 'NO'
	return op_str, next_push


def main():
	max_num = int(read().strip())
	stack = []
	next_push = 1
	op_str = []
	for current in range(max_num):
		num_in = int(read().strip())
		op_str, next_push = stack_op(num_in, stack, next_push, op_str)
		if op_str == 'NO':
			break
	if op_str == 'NO':
		print(op_str)
	else:
		for letter in op_str:
			print(letter)


def file_main():
	file = open('baekjoon_1874_input1.txt', mode='r', encoding='utf-8')
	max_num = int(file.readline().strip())
	stack = []
	next_push = 1
	op_str = []
	for current in range(max_num):
		num_in = int(file.readline().strip())
		op_str, next_push = stack_op(num_in, stack, next_push, op_str)
		if op_str == 'NO':
			break
	if op_str == 'NO':
		print(op_str)
	else:
		for letter in op_str:
			print(letter)
	file.close()


if __name__ == '__main__':
	main()
