# https://leetcode.com/problems/single-number/
# Solved Date: 20.04.02.
# 내부에는 중복 제거를 한 sum을 두배해서 뺀 값을 통해 구하는 방법과 bit연산이... 있었다.

import sys
read = sys.stdin.readline


def set_single_number(nums):
	num_set = set()
	for number in nums:
		if number in num_set:
			num_set.remove(number)
		else:
			num_set.add(number)
	return num_set.pop()


def main():
	nums = [int(x) for x in read().split()]
	print(set_single_number(nums))


if __name__ == '__main__':
	main()
