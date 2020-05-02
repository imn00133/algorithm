# https://www.acmicpc.net/problem/11726
# Solved Date: 20.03.30.

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MOD_NUM = 10007
dp_arr = [0 for _ in range(1001)]


def bottom_up(num):
	dp_arr[0] = dp_arr[1] = 1
	for index in range(2, num+1):
		dp_arr[index] = (dp_arr[index-1] + dp_arr[index-2]) % MOD_NUM
	return dp_arr[num]


def top_down(num):
	if num == 1 or num == 0:
		return 1
	if dp_arr[num] > 0:
		return dp_arr[num]
	dp_arr[num] = (top_down(num-1) + top_down(num-2)) % MOD_NUM
	return dp_arr[num]


def main(mode=''):
	num = int(read().strip())
	if mode == 'top':
		print(top_down(num))
	else:
		print(bottom_up(num))


if __name__ == '__main__':
	main()
