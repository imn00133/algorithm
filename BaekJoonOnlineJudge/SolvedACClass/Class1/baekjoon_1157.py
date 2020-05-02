# https://www.acmicpc.net/problem/1157
# Solved Date: 20.04.02.

import sys
read = sys.stdin.readline

alpha_count = [0 for _ in range(26)]


def pythonic(count_str):
	import string
	alpha_list = string.ascii_uppercase
	count_str = count_str.upper()
	for index, letter in enumerate(alpha_list):
		alpha_count[index] = count_str.count(letter)
	max_num = max(alpha_count)
	if alpha_count.count(max_num) != 1:
		max_letter = '?'
	else:
		max_letter = alpha_list[alpha_count.index(max_num)]
	return max_letter


def legacy(string):
	string = string.upper()
	for letter in string:
		alpha_count[ord(letter)-ord('A')] += 1
	max_num = max(alpha_count)
	if alpha_count.count(max_num) != 1:
		max_letter = '?'
	else:
		max_letter = chr(alpha_count.index(max_num) + ord('A'))
	return max_letter


def main(mode=''):
	string = read().strip()
	if mode == 'legacy':
		print(legacy(string))
	else:
		print(pythonic(string))


if __name__ == '__main__':
	main('legacy')
