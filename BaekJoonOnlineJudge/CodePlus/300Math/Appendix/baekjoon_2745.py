# https://www.acmicpc.net/problem/2745
# Solved Date: 20.04.01.
# 재귀로도 풀 수 있으나, 재귀의 범위가 커서 반복으로 해결하였다.

import sys

read = sys.stdin.readline


def legacy_decode(num, base):
	decimal = 0
	for i in range(len(num)):
		letter = num[-(i+1)]
		if ord('0') <= ord(letter) <= ord('9'):
			decimal += int(letter) * (base ** i)
		else:
			value = ord(letter) - ord('A') + 10
			decimal += value * (base ** i)
	return decimal


def pythonic_decode(num, base):
	return int(num, base)


def main(mode=''):
	num, base = read().split()
	base = int(base)
	convert_decimal = pythonic_decode
	if mode == 'legacy':
		convert_decimal = legacy_decode
	print(convert_decimal(num, base))


if __name__ == '__main__':
	main('legacy')
