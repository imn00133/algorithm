"""
Solving Date: 20.01..
site: https://algospot.com/judge/problem/read/QUADTREE
적혀있지 않으나 본 문제는 트리 자료구조를 사용하며, 전위순환을 한다.
compress, decompress를 할 수 있는 함수를 제작함
"""


def decompress(string, y, x, size):
	# 본 함수에서는 반복자(iterator)를 사용한다.
	# 자세한 내용은 https://dojang.io/mod/page/view.php?id=2405를 참고한다.
	head = string.__iter__()
	# 기저사례: 첫 글자가 b또는 w인 경우
	if head == 'b' or head == 'w':
		pass


def main():
	case_num = int(input())
	for _ in range(case_num):
		tree = input()


def file_main():
	input_file = open("2_test.txt")
	output_file = open("2_test_ans.txt")
	case_num = int(input_file.readline().strip())
	for _ in range(case_num):
		tree = input_file.readline().strip()


if __name__ == "__main__":
	main()
