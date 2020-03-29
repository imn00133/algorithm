# https://www.acmicpc.net/problem/1212
# Date: 20.03.29.

import sys
read = sys.stdin.readline
OCTAL_TABLE = ('000', '001', '010', '011', '100', '101', '110', '111')


def used_tuple(octal):
	binary = []
	for oct_num in octal:
		binary.append(OCTAL_TABLE[int(oct_num)])
	for _ in range(2):
		if binary[0][0] == '0':
			binary[0] = binary[0][1:]
	return ''.join(binary)


def legacy(octal):
	binary = []
	for oct_num in octal:
		oct_num = int(oct_num)
		temp_bin = []
		for _ in range(3):
			temp_bin.append(oct_num % 2)
			oct_num //= 2
		binary.extend(reversed(temp_bin))
	for _ in range(2):
		if binary[0] == 0:
			binary.pop(0)
	binary = [str(x) for x in binary]
	return ''.join(binary)


def pythonic(octal):
	octal = int(octal, 8)
	return format(octal, 'b')


def main():
	octal = read().strip()
	binary = used_tuple(octal)
	print(binary)


if __name__ == '__main__':
	main()
