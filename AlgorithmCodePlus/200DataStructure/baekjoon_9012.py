# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline


def valid_par_str(par_str):
	stack_cnt = 0
	for letter in par_str:
		if letter == '(':
			stack_cnt += 1
		elif stack_cnt != 0:
			stack_cnt -= 1
		else:
			return False
	if stack_cnt == 0:
		return True
	else:
		return False


def main():
	test_case_num = int(input().strip())
	for test_num in range(test_case_num):
		parenthesis_str = input().strip()
		if valid_par_str(parenthesis_str):
			print("YES")
		else:
			print("NO")


def file_main():
	file = open("baekjoon_9012_input.txt", mode='r', encoding='utf-8')
	test_case_num = int(file.readline().strip())
	for test_num in range(test_case_num):
		parenthesis_str = file.readline().strip()
		if valid_par_str(parenthesis_str):
			print("YES")
		else:
			print("NO")


if __name__ == '__main__':
	main()
