# https://www.acmicpc.net/problem/10799
# Solving Date: 20.03.24.

import sys
read = sys.stdin.readline


def index_laser(stick):
	stack = []
	cut_number = 0
	for index, block in enumerate(stick):
		if block == '(':
			stack.append(index)
		elif index - 1 == stack[-1]:
			stack.pop()
			cut_number += len(stack)
		else:
			stack.pop()
			cut_number += 1
	return cut_number


def laser(stick):
	stack = []
	cut_number = 0
	used_laser = False
	for block in stick:
		if block == '(':
			used_laser = False
			stack.append('(')
		elif used_laser:
			stack.pop()
			cut_number += 1
		else:
			stack.pop()
			used_laser = True
			cut_number += len(stack)
	return cut_number


def main(mode=''):
	if mode:
		file = open("baekjoon_10799_input.txt", mode='r', encoding='utf-8')
		while True:
			stick = file.readline().strip()
			if not stick:
				break
			cut_number = index_laser(stick)
			print(cut_number)
		file.close()
	else:
		stick = read().strip()
		cut_number = index_laser(stick)
		print(cut_number)


if __name__ == '__main__':
	main()
