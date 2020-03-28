# https://www.acmicpc.net/problem/1978

import sys
read = sys.stdin.readline


def discriminate_prime(value):
	if value < 2:
		return False
	# 실수 계산을 하지 않기 위해, 조건을 i*i <= n으로 변경할 수도 있다.
	for divisor in range(2, int(value**0.5)+1):
		if value % divisor == 0:
			return False
	return True


def main():
	test_case_num = int(read().strip())
	test_list = [int(x) for x in read().split()]
	prime_count = 0
	for value in test_list:
		if discriminate_prime(value):
			prime_count += 1
	print(prime_count)


if __name__ == '__main__':
	main()
