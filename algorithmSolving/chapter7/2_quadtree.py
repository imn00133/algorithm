"""
Solving Date: 20.01..
site: https://algospot.com/judge/problem/read/QUADTREE
적혀있지 않으나 본 문제는 트리 자료구조를 사용하며, 전위순환을 한다.
"""


def rev_str(string, head):
	"""
	본 함수에서는 반복자(iterator)를 사용한다.
	자세한 내용은 https://dojang.io/mod/page/view.php?id=2405를 참고한다.
	:param string: 쿼드트리 원문
	:param head: 쿼드트리의 iterator를 인자로 받는다.
	:return: 뒤집힌 쿼드트리 반환
	"""
	head.__next__()
	if head == 'b' or head == 'w':
		return string[1, head]
	upper_left = rev_str(string)


def main():
	
	case_num = int(input())
	for _ in range(case_num):
		tree = input()
		rev_tree = rev_str(tree, tree.__iter__())
		print(rev_tree)


def file_main():
	input_file = open("2_test.txt")
	output_file = open("2_test_ans.txt")
	case_num = int(input_file.readline().strip())
	for _ in range(case_num):
		tree = input_file.readline().strip()
		rev_tree = rev_str(tree, tree.__iter__())
		if rev_tree == output_file.readline().strip():
			print("정답")
		else:
			print("오류")


if __name__ == "__main__":
	main()
