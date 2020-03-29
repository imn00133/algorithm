# https://www.acmicpc.net/problem/1676


def main():
	num = int(input())
	count_five = 0
	squared = 1
	while 5 ** squared <= num:
		count_five += num // (5 ** squared)
		squared += 1
	print(count_five)


if __name__ == '__main__':
	main()
