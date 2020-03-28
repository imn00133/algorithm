# https://www.acmicpc.net/problem/1929

import sys
read = sys.stdin.readline


def main():
	start, end = (int(x) for x in read().split())
	prime_check = [True for _ in range(end+1)]
	prime_check[0] = prime_check[1] = False
	for number in range(2, int(end**0.5)+1):
		if prime_check[number]:
			for remove in range(number**2, end+1, number):
				prime_check[remove] = False

	for index in range(start, end+1):
		if prime_check[index]:
			print(index)


if __name__ == '__main__':
	main()
