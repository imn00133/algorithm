# https://www.acmicpc.net/problem/1676


def main():
	num = int(input())
	count_5 = 0
	squared = 1
	while 5 ** squared <= num:
		count_5 += num // (5 ** squared)
		squared += 1
	print(count_5)


if __name__ == '__main__':
	main()
