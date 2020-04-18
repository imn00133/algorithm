# https://www.acmicpc.net/problem/1699
# Solved Date: 20.04.02.
# 본 문제의 시간초과는 파이썬의 제곱 연산이 느린 것으로 보인다.
# 해결방식은 diary를 참고한다.

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 100000
dp_arr = [x for x in range(MAX+1)]


def bottom_up(num):
	for index in range(1, num+1):
		for value in range(1, index):
			square = value ** 2
			if square > index:
				break
			if dp_arr[index - square] + 1 < dp_arr[index]:
				dp_arr[index] = dp_arr[index - square] + 1


def top_down(num):
	if dp_arr[num] < num:
		return dp_arr[num]
	if num == 0:
		dp_arr[0] = 0
		return dp_arr[num]
	for index in range(1, num+1):
		square = index ** 2
		if square > index:
			break
		if top_down(num - square) + 1 < dp_arr[num]:
			dp_arr[num] = dp_arr[num - square] + 1
	return dp_arr[num]


def main(mode=''):
	num = int(read().strip())
	if mode == 'top':
		top_down(num)
	else:
		bottom_up(num)
	print(dp_arr[num])


if __name__ == '__main__':
	main()
