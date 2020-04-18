# https://www.acmicpc.net/problem/1935
# Solving Date: 20.03.27.
# ascii를 통해 배열의 크기를 줄임
# https://lsjsj92.tistory.com/201

import sys
read = sys.stdin.readline


def calc(stack, operand):
	b = stack.pop()
	a = stack.pop()
	ret = 0
	if operand == ord('*'):
		ret = a * b
	elif operand == ord('/'):
		ret = a / b
	elif operand == ord('+'):
		ret = a + b
	elif operand == ord('-'):
		ret = a - b
	return ret


def store_calc(expression, number):
	stack = []
	for operand in expression:
		if ord('A') <= operand <= ord('Z'):
			stack.append(number[operand-ord('A')])
		else:
			stack.append(calc(stack, operand))
	return stack.pop()


def main(mode=''):
	if mode == 'f':
		file = open("baekjoon_1935_input2.txt", mode='r', encoding='utf-8')
		operand_num = int(file.readline().strip())
		expression = [ord(x) for x in list(file.readline().strip())]
		number = []
		for _ in range(operand_num):
			number.append(int(file.readline().strip()))
		print("{0:.2f}".format(store_calc(expression, number)))
		file.close()
	else:
		operand_num = int(read().strip())
		expression = [ord(x) for x in list(read().strip())]
		number = []
		for _ in range(operand_num):
			number.append(int(read().strip()))
		print("{0:.2f}".format(store_calc(expression, number)))


if __name__ == '__main__':
	main()
