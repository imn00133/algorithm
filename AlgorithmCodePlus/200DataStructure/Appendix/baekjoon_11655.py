# https://www.acmicpc.net/problem/11655


def calc_rot(ascii_value, start_ascii, end_ascii):
	if ascii_value + 13 > end_ascii:
		# 더해서 26이 되었을 때 start_ascii가 되어야 한다.
		letter = start_ascii + (ascii_value + 12 - end_ascii)
	else:
		letter = ascii_value + 13
	return chr(letter)


def main():
	string = input()
	conversion_rot = []
	for letter in string:
		ascii_value = ord(letter)
		rot = 13
		if ord('A') <= ascii_value <= ord('Z'):
			conversion_rot.append(calc_rot(ascii_value, ord('A'), ord('Z')))
		elif ord('a') <= ascii_value <= ord('z'):
			conversion_rot.append(calc_rot(ascii_value, ord('a'), ord('z')))
		else:
			conversion_rot.append(letter)
	print(''.join(conversion_rot))


if __name__ == '__main__':
	main()
