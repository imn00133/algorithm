# https://www.acmicpc.net/problem/10430

import sys
read = sys.stdin.readline


def main():
	a, b, c = (int(x) for x in read().split())
	print((a + b) % c)
	print(((a % c) + (b % c)) % c)
	print((a * b) % c)
	print(((a % c) * (b % c)) % c)


if __name__ == '__main__':
	main()
