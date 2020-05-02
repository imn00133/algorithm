# https://www.acmicpc.net/problem/6588
# Solving Date: 20.03.29.
# print를 썼을 때는 4200ms가 나오다가 read를 쓰니 280ms가 나온다.
# range의 초기값, 최대값, step을 잘 사용하자.
# 최대값은 상수에 놓고 사용하자.

# 17103을 해결하면서 발견한 점
# prime_list는 1000이하의 소수만 들어있다. 그런데 1000000이하의 2를 제외한 짝수에서는 테스트가 통과된다.

import sys
read = sys.stdin.readline

MAX = 1000000


def eratosthenes(prime_list, check_prime):
	check_prime[0] = check_prime[1] = False
	for number in range(2, int(MAX**0.5)+1):
		if check_prime[number]:
			prime_list.append(number)
			for remove_index in range(number**2, MAX+1, number):
				check_prime[remove_index] = False
			# squared = number ** 2
			# while squared <= MAX:
			# 	check_prime[squared] = False
			# 	squared += number


def main():
	prime_list = []
	check_prime = [True for _ in range(MAX+1)]
	eratosthenes(prime_list, check_prime)
	while True:
		test_number = int(read().strip())
		if not test_number:
			break
		string = ""
		for prime in prime_list:
			couple_prime = test_number - prime
			if check_prime[couple_prime]:
				string = "{0} = {1} + {2}".format(test_number, prime, couple_prime)
				break
			elif prime * 2 > test_number:
				string = "Goldbach's conjecture is wrong"
				break
		print(string)


if __name__ == '__main__':
	main()
