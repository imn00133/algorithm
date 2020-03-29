# https://www.acmicpc.net/problem/9613

import sys


def gcd(num1, num2):
	while num2 != 0:
		r = num1 % num2
		num1 = num2
		num2 = r
	return num1


def recursive_gcd_sum(num_list):
	gcd_sum = 0
	if len(num_list) == 1:
		return 0
	for num2 in num_list[1:]:
		gcd_sum += gcd(num_list[0], num2)
	return gcd_sum + recursive_gcd_sum(num_list[1:])


def main(mode=''):
	read = sys.stdin.readline
	file = None
	if mode == 'f':
		file = open("baekjoon_9613_input.txt", mode='r', encoding='utf-8')
		read = file.readline
	test_case_num = int(read().strip())
	for _ in range(test_case_num):
		num_list = [int(x) for x in read().split()]
		gcd_sum = recursive_gcd_sum(num_list[1:])
		print(gcd_sum)
	if mode == 'f':
		file.close()


if __name__ == '__main__':
	main()
