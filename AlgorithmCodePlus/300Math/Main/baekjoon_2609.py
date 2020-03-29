# https://www.acmicpc.net/problem/2609
# Solving Date: 20.03.26.
# 재귀함수로 할 때는, 값이 끝까지 return되도록 주의할 것
# 재귀나 반복이나 속도차이는 없었음

import sys
read = sys.stdin.readline


def gcd(a, b):
	while b:
		r = a % b
		a = b
		b = r
	return a


def recursion_gcd(a, b):
	if b == 0:
		return a
	else:
		return recursion_gcd(b, a % b)


def lcm(a, b, calc_gcd):
	return int(a / calc_gcd * b)


def main(mode=''):
	a, b = (int(x) for x in read().split())
	if mode == 'r':
		calc_gcd = recursion_gcd(a, b)
	else:
		calc_gcd = gcd(a, b)
	print(calc_gcd)
	print(lcm(a, b, calc_gcd))


if __name__ == '__main__':
	main()
