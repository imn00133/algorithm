# https://www.acmicpc.net/problem/2884

import sys
read = sys.stdin.readline


def main():
	hour, minute = (int(x) for x in (read().split()))
	minute -= 45
	if minute < 0:
		hour -= 1
		minute += 60
	if hour < 0:
		hour += 24
	print(hour, minute)


if __name__ == '__main__':
	main()
