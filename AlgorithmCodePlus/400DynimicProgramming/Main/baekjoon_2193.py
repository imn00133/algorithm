# https://www.acmicpc.net/problem/2193
# Solved Date: 20.03.31.

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 90
dp_arr = [[0 for _ in range(2)] for _ in range(MAX+1)]


def bottom_up(num):
	dp_arr[1][1] = 1
	for index in range(2, num+1):
		dp_arr[index][0] = dp_arr[index-1][0] + dp_arr[index-1][1]
		dp_arr[index][1] = dp_arr[index-1][0]
	return sum(dp_arr[num])


def calc(num, i):
	if num == 1 or dp_arr[num][i] > 0:
		return dp_arr[num][i]
	if i == 0:
		dp_arr[num][i] = calc(num-1, 0) + calc(num-1, 1)
	else:
		dp_arr[num][i] = calc(num-1, 0)
	return dp_arr[num][i]


def top_down(num):
	dp_arr[1][1] = 1
	for i in range(2):
		calc(num, i)
	return sum(dp_arr[num])


def main(mode=''):
	num = int(read().strip())
	if mode == 'top':
		print(top_down(num))
	else:
		print(bottom_up(num))


if __name__ == '__main__':
	main('top')
