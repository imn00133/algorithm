"""
chapter7의 도입에 있는 곱셈 프로그램 구현
O(n^2)과 O(n^log3)의 속도, 일반적인 python의 곱셈 속도도 비교
input, output을 normalize하는 시간은 포함하지 않았다.

만든 곱셈의 속도가 훨씬 느린 것을 볼 수 있는데, 이는 list로 입출력하기 때문이다.
제대로 구현할 수 있나... 흐음...

time을 통한 속도 비교(decorator사용)
https://m.blog.naver.com/cjh226/221392127142
https://jeongukjae.github.io/posts/python%EC%97%90%EC%84%9C-%EC%8B%9C%EA%B0%84%EC%B8%A1%EC%A0%95%ED%95%98%EA%B8%B0/

timeit 참고사이트(코드가 너무 길어져서 사용 안함)
https://devluna.blogspot.com/2015/09/python-code-timeit.html
https://docs.python.org/ko/3/library/timeit.html

곱샘프로그램의 입출력은 각 수의 자릿수가 1의 자리에서부터 시작해서 저장
ex) 1multiply([3, 2, 1], [6, 5, 4] = 123 * 456 = 56088 = [8, 8, 0, 6, 5]
"""
import time
import string
import random


def logging_time(original_fn):
	def wrapper_fn(*args, **kwargs):
		start_time = time.time()
		result = original_fn(*args, **kwargs)
		end_time = time.time()
		print("Working Time[{0}]: {1:.6f} sec".format(original_fn.__name__, end_time - start_time))
		return result
	return wrapper_fn


def random_num(digit=6):
	"""
	자리수만큼의 숫자 랜덤 제작
	:param digit: 자리수
	:return result: string로 구성된 숫자
	"""
	# https://hongku.tistory.com/297
	result = ""
	result += random.choice(string.digits[1:])
	for _ in range(digit-1):
		result += random.choice(string.digits)
	return result


def input_normalize(num):
	num = " ".join(num).split()
	num.reverse()  
	num = list(map(int, num))
	return num


def output_normalize(num):
	num.reverse()
	num = list(map(str, num))
	num = int("".join(num))
	return num


def normalize(num):
	num.append(0)
	for i in range(len(num)-1):
		# karatsuba를 사용하기 위한 버림 계산
		if num[i] < 0:
			borrow = (abs(num[i]) + 9) // 10
			num[i+1] -= borrow
			num[i] += 10
		else:
			num[i+1] += num[i] // 10
			num[i] %= 10
	while True:
		if len(num) > 1 and num[-1] == 0:
			num.pop()
		else:
			return num


def add_to(num1, num2, k):
	# a += b*(10^k)구현
	# bit연산을 해야하나, list연산을 함
	ans = [0 for _ in range(k)]
	ans.extend(num2)
	if len(num1) > len(ans):
		ans, num1 = num1, ans
	for i in range(len(num1)):
		ans[i] = num1[i] + ans[i]
	return ans


def sub_from(num1, num2):
	# a -= b를 구현 a
	if len(num1) < len(num2):
		num1, num2 = num2, num1
	for i in range(len(num2)):
		num1[i] = num1[i] - num2[i]
	num1 = normalize(num1)
	return num1


def karatsuba(num1, num2, loop=1):
	# 재귀로 인해 logging이 불가하여 따로 처리함
	# 1이 2보다 짧을 경우 바꿈
	if len(num1) < len(num2):
		return karatsuba(num2, num1)
	# 1이나 2가 비어 있는 경우
	if len(num1) == 0 or len(num2) == 0:
		return [0]
	# 짧을 경우, 일반 곱셈을 함(책에서는 50이나 반복횟수상 줄임)
	if len(num1) <= 10:
		return multiply_nolog(num1, num2)
	half = len(num1)//2
	# num1, 2를 밑에서 half자리와 나머지로 분리
	num1_0 = num1[:half]
	num1_1 = num1[half:]
	num2_0 = num2[:min(len(num2), half)]
	num2_1 = num2[min(len(num2), half):]
	# z2 = a1 * b1
	z2 = karatsuba(num1_1, num2_1)
	# z0 = a0 * b0
	z0 = karatsuba(num1_0, num2_0)
	# ret1 = a0+a1, ret2 = b0+b1
	ret1 = add_to(num1_0, num1_1, 0)
	ret2 = add_to(num2_0, num2_1, 0)
	# z1 = (ret1 * ret2) - z0 -z2
	z1 = karatsuba(ret1, ret2)
	z1 = sub_from(z1, z0)
	z1 = sub_from(z1, z2)
	# ret = z0 + z1 * 10^half + z2 * 10^(half*2)
	ans = [0]
	ans = add_to(ans, z0, 0)
	ans = add_to(ans, z1, half)
	ans = add_to(ans, z2, half*2)
	ans = normalize(ans)
	return ans


def multiply_nolog(num1, num2, loop=1):
	# karakuba에서 사용할 log없는 함수
	ans = []
	for _ in range(loop):
		ans = [0 for _ in range(len(num1) + len(num2) + 1)]
		for i in range(len(num1)):
			for j in range(len(num2)):
				ans[i+j] += num1[i]*num2[j]
	ans = normalize(ans)
	return ans


@logging_time
def multiply(num1, num2, loop=1):
	# 가장 큰 수를 더했을 때, 최대 크기는 각 자리수의 덧셈, +1은 왜 했을까?
	ans = []
	for _ in range(loop):
		ans = [0 for _ in range(len(num1) + len(num2) + 1)]
		for i in range(len(num1)):
			for j in range(len(num2)):
				ans[i+j] += num1[i]*num2[j]
	ans = normalize(ans)
	return ans


@logging_time
def python_multiply(num1, num2, loop=1):
	# 일반적인 python에서의 곱셈
	num1, num2 = int(num1), int(num2)
	ans = 0
	for _ in range(loop):
		ans = num1 * num2
	return ans


def init_value():
	# 클로저가 필요한데 포기. 대충 하자.
	digit = input("생성할 숫자 자리수를 입력하세요(기본값 6자리):")
	if digit == "":
		num = random_num()
	else:
		num = random_num(int(digit))
	return num


def main():
	# 1번으로는 시간이 계산되지 않아, 50000번 반복한다.
	loop = 50000
	num1 = init_value()
	print("생성된 숫자 1: " + num1)
	num2 = init_value()
	print("생성된 숫자 2: " + num2)

	# python에서 사용하는 곱셈
	py_mul = python_multiply(num1, num2, loop)
	print(py_mul)

	# list로 만든 일반 곱셈
	num1 = input_normalize(num1)
	num2 = input_normalize(num2)
	on2_mul = multiply(num1, num2, loop)
	on2_mul = output_normalize(on2_mul)
	print(on2_mul)

	# 카라츠바 정수 곱셈
	start_time = time.time()
	for _ in range(loop):
		kara_mul = karatsuba(num1, num2, loop)
	end_time = time.time()
	print("Working Time[{0}]: {1:.6f} sec".format("karatsuba", end_time - start_time))
	kara_mul = output_normalize(kara_mul)
	print(kara_mul)


if __name__ == "__main__":
	main()
