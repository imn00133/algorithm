# https://www.acmicpc.net/problem/9093
# list연산이 적게 들어가서 그런지 더 빠르다.

import sys
input = sys.stdin.readline


def main():
	test_case_num = int(input().strip())
	for test_num in range(test_case_num):
		word_list = input().split()
		reverse_str = ""
		for word in word_list:
			reverse_str += word[::-1]
			reverse_str += " "
		print(reverse_str)


def file_main():
	file = open("baekjoon_9093_input.txt", mode='r', encoding='utf-8')
	test_case_num = int(file.readline().strip())
	for test_num in range(test_case_num):
		word_list = file.readline().split()
		reverse_str = ""
		for word in word_list:
			reverse_str += word[::-1]
			reverse_str += " "
		print(reverse_str)
	file.close()


if __name__ == '__main__':
	main()
