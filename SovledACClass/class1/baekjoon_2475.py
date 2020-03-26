# https://www.acmicpc.net/problem/2475

import sys
read = sys.stdin.readline


def main():
	in_list = [int(x) for x in read().split()]
	valid_num = sum([x**2 for x in in_list]) % 10
	print(valid_num)


if __name__ == '__main__':
	main()
