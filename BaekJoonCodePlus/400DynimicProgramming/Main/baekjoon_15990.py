# https://www.acmicpc.net/problem/15990
# Solved Date: 20.03.31.
# 재귀함수는 http://blog.naver.com/mirusu400/221788252855의 도움을 받았다.

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 100000
MOD = 1000000009
dp_arr = [[0 for _ in range(4)] for _ in range(MAX+1)]


def bottom_up(num):
	dp_arr[1][1] = dp_arr[2][2] = dp_arr[3][3] = 1
	for i in range(1, num+1):
		if i > 1:
			dp_arr[i][1] = (dp_arr[i-1][2] + dp_arr[i-1][3]) % MOD
		if i > 2:
			dp_arr[i][2] = (dp_arr[i-2][1] + dp_arr[i-2][3]) % MOD
		if i > 3:
			dp_arr[i][3] = (dp_arr[i-3][1] + dp_arr[i-3][2]) % MOD


def get(num, i):
	if num <= 3 or dp_arr[num][i] > 0:
		return dp_arr[num][i]
	if i == 1:
		dp_arr[num][i] = (get(num - i, 2) + get(num - i, 3)) % MOD
	elif i == 2:
		dp_arr[num][i] = (get(num - i, 1) + get(num - i, 3)) % MOD
	else:
		dp_arr[num][i] = (get(num - i, 1) + get(num - i, 2)) % MOD
	return dp_arr[num][i]


def top_down(num):
	dp_arr[1][1] = dp_arr[2][2] = dp_arr[3][1] = dp_arr[3][2] = dp_arr[3][3] = 1
	for i in range(1, 4):
		get(num, i)
	# 마지막까지 돌렸을 때, num-2의 2와  num-1의 1은 계산하지 않아, 추가하였다.
	get(num-2, 2)
	get(num-1, 1)


def main(mode=''):
	test_case_num = int(read().strip())
	if mode == '':
		bottom_up(MAX)
	for _ in range(test_case_num):
		num = int(read().strip())
		if mode == 'top':
			if num >= 1000:
				for part_num in range(1000, num + 1, 1000):
					top_down(part_num)
			top_down(num)
		print(sum(dp_arr[num]) % MOD)


if __name__ == '__main__':
	main('top')
