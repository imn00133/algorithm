# https://www.acmicpc.net/problem/1373
# 진수변환은 https://www.daleseo.com/python-int-bases/를 참고한다.
# n진법 string을 10진법 숫자로 표현하는 방법은 https://programmers.co.kr/learn/courses/4008/lessons/12733

import sys
read = sys.stdin.readline


def legacy(binary):
	if len(binary) % 3 != 0:
		binary = ("0" * (3 - (len(binary) % 3))) + binary
	octal = []
	for index in range(0, len(binary), 3):
		split_binary = binary[index:index+3]
		temp_octal = 0
		for num in range(len(split_binary)):
			temp_octal += int(split_binary[num]) * (2 ** (2 - num))
		octal.append(temp_octal)
	octal = [str(x) for x in octal]
	return ''.join(octal)


def pythonic(binary):
	binary = int(binary, 2)
	return format(binary, 'o')


def main():
	binary = read().strip()
	octal = legacy(binary)
	print(octal)


if __name__ == '__main__':
	main()
