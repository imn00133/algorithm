# https://www.acmicpc.net/problem/17103
# Solving Date: 20.03.29.

import sys
read = sys.stdin.readline
MAX_NUM = 1000000


def Erastos(check_prime):
	check_prime[0] = check_prime[1] = False
	for num in range(int(MAX_NUM**0.5) + 1):
		if check_prime[num]:
			for remove_num in range(num**2, MAX_NUM+1, num):
				check_prime[remove_num] = False
	prime_list = [x for x in range(MAX_NUM+1) if check_prime[x]]
	return prime_list


def main():
	check_prime = [True for _ in range(MAX_NUM+1)]
	prime_list = Erastos(check_prime)
	test_case_num = int(read().strip())
	for _ in range(test_case_num):
		partition = 0
		num = int(read().strip())
		for prime in prime_list:
			if prime > int(num/2):
				break
			if check_prime[num-prime]:
				partition += 1
		print(partition)


if __name__ == '__main__':
	main()
