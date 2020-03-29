# https://www.acmicpc.net/problem/11720

import sys
read = sys.stdin.readline


def main():
	num_count = int(read().strip())
	num_string = read().strip()
	sum_string = 0
	for index in range(num_count):
		sum_string += int(num_string[index])
	print(sum_string)


if __name__ == '__main__':
	main()
