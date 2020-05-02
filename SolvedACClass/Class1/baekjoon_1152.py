# https://www.acmicpc.net/problem/1152
# Solved Date: 20.04.02.

import sys
read = sys.stdin.readline


def legacy(string):
	# 아예 없을 때
	if not string:
		return 0
	word = 1
	for letter in string:
		if letter == ' ':
			word += 1
	return word


def main(mode=''):
	if mode == 'legacy':
		print(legacy(read().strip()))
	else:
		string = read().split()
		print(len(string))


if __name__ == '__main__':
	main('legacy')
