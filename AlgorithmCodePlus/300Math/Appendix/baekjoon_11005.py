# https://www.acmicpc.net/problem/11005
# Solved Date: 20.04.01.
# stirng모듈에서 모든 알파벳 출력하는 상수 사용하기
# https://programmers.co.kr/learn/courses/4008/lessons/12729

import sys
import string

read = sys.stdin.readline
DIGIT = list(string.digits) + list(string.ascii_uppercase)


def main():
	num, base = (int(x) for x in read().split())
	convert_num = []
	while num:
		convert_num.append(DIGIT[num % base])
		num //= base
	print(''.join(reversed(convert_num)))


if __name__ == '__main__':
	main()
