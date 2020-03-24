# https://www.acmicpc.net/problem/10799

import sys
read = sys.stdin.readline


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
			cut_number = laser(stick)
			print(cut_number)
		file.close()
	else:
		stick = read().strip()
		cut_number = laser(stick)
		print(cut_number)


if __name__ == '__main__':
	main()
