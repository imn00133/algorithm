# https://www.acmicpc.net/problem/1934
# Solving Date: 20.03.26.

import sys
read = sys.stdin.readline


def gcm(a, b):
	while b:
		r = a % b
		a = b
		b = r
	return a


def lcm(a, b):
	return int(a / gcm(a, b) * b)


def main(mode=''):
	if mode == 'f':
		file = open("baekjoon_1934_input.txt", mode='r', encoding='utf-8')
		test_case_num = int(file.readline().strip())
		for _ in range(test_case_num):
			a, b = (int(x) for x in file.readline().split())
			print(lcm(a, b))
		file.close()
	else:
		test_case_num = int(read().strip())
		for _ in range(test_case_num):
			a, b = (int(x) for x in read().split())
			print(lcm(a, b))


if __name__ == '__main__':
	main()
