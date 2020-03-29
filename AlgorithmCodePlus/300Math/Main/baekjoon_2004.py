# https://www.acmicpc.net/problem/2004


def count_squared_num(num, divisor):
	count = 0
	squared = 1
	while divisor ** squared <= num:
		count += num // (divisor ** squared)
		squared += 1
	return count


def return_count_num(n, m, divisor):
	calc_n = count_squared_num(n, divisor)
	calc_n_m = count_squared_num(n - m, divisor)
	calc_m = count_squared_num(m, divisor)
	return calc_n - calc_n_m - calc_m


def main():
	n, m = (int(x) for x in input().split())
	count_two = return_count_num(n, m, 2)
	count_five = return_count_num(n, m, 5)
	print(min(count_two, count_five))


if __name__ == '__main__':
	main()
