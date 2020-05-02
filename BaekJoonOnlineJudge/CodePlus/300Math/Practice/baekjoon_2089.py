# https://www.acmicpc.net/problem/2089
# Solving Date: 20.03.29.

import sys
read = sys.stdin.readline


def cal_neg_bin(num):
	binary = []
	while num != 1:
		if num % 2 == 1:
			binary.append((num % -2) + 2)
			num = num // -2 + 1
		else:
			binary.append(num % -2)
			num //= -2
	binary.append(1)
	binary = [str(x) for x in binary]
	return ''.join(reversed(binary))


def main():
	num = int(read().strip())
	negative_binary = 0
	if num:
		negative_binary = cal_neg_bin(num)
	print(negative_binary)


if __name__ == '__main__':
	main()

