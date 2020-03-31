# https://www.acmicpc.net/problem/11052
# Solved Date: 20.03.31.

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

MAX = 1000
dp_arr = [0 for _ in range(MAX+1)]


def bottom_up(num, card_pack):
	dp_arr[1] = card_pack[1]
	for index in range(2, num+1):
		for j in range(1, index+1):
			dp_arr[index] = max(dp_arr[index], dp_arr[index-j] + card_pack[j])
	return dp_arr[num]


def top_down(num, card_pack):
	if num == 1:
		return card_pack[num]
	if dp_arr[num] > 0:
		return dp_arr[num]
	for index in range(1, num+1):
		dp_arr[num] = max(dp_arr[num], top_down(num-index, card_pack) + card_pack[index])
	return dp_arr[num]


def main(mode=''):
	purchase_num = int(read().strip())
	card_pack = [0]
	temp_pack = read().split()
	card_pack.extend([int(x) for x in temp_pack])
	if mode == 'top':
		print(top_down(purchase_num, card_pack))
	else:
		print(bottom_up(purchase_num, card_pack))


if __name__ == '__main__':
	main()
