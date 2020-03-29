# https://www.acmicpc.net/problem/9093
# Solving Date: 20.03.21.
# stack을 안 쓰는게 더 빠르다.

import sys
input = sys.stdin.readline


def stack_all_pop(stack):
	reverse_word = ""
	for i in range(len(stack)):
		reverse_word += stack.pop()
	return reverse_word


def reverse_string(string):
	stack = []
	rev_str = ""
	for letter in string:
		if letter == " ":
			rev_str += stack_all_pop(stack)
			rev_str += " "
		elif letter == "\n":
			rev_str += stack_all_pop(stack)
		else:
			stack.append(letter)
	return rev_str


def main():
	test_case_num = int(input().strip())
	for test_num in range(test_case_num):
		string = input().strip() + "\n"
		rev_str = reverse_string(string)
		print(rev_str)


def file_main():
	file = open("baekjoon_9093_input.txt", mode='r', encoding='utf-8')
	test_case_num = int(file.readline().strip())
	for test_num in range(test_case_num):
		string = file.readline().strip() + "\n"
		rev_str = reverse_string(string)
		print(rev_str)
	file.close()


if __name__ == "__main__":
	main()
