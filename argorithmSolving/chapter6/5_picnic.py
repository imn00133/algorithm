def initiate(student, friend_num, friend_list):
	# 순서는 열, 행
	# are_friends = 친구를 행렬로 나타냄
	are_friends = [[False for _ in range(student)] for _ in range(student)]
	for i in range(0, friend_num * 2, 2):
		are_friends[friend_list[i]][friend_list[i + 1]] = True
		are_friends[friend_list[i + 1]][friend_list[i]] = True
	# taken[i] =  i번째 학생의 짝을 찾으면 True
	taken = [False for _ in range(student)]
	return are_friends, taken


def count_pairing(are_friends, taken):
	# are_friends는 global이 나을 수도...
	first_student = -1
	for i in range(len(taken)):
		if not taken[i]:
			first_student = i
			break
	# 기저 사례: 모든 학생이 짝을 찾으면 한 가지 방법을 찾아서 종료
	# all을 사용할 수 있으나, 앞쪽에서 검사를 했기 때문에 반복 검사하지 않는다.
	if first_student == -1:
		return 1
	ret = 0
	# 전체를 순환하면서 돌면 같은 학생 짝 두 번 짓는 것, 다른 순서로 학생들을 짝짓는 것을 해소해야함
	# 두 번째 검사의 시작을 i 이후만 잡으면 다른 순서로 학생을 짝 짓는 것이 포함됨
	# 따라서 처음 사람을 지정하고 나머지 사람에 대해서 계산하도록 프로그램을 변경
	for pair_with in range(first_student + 1, len(taken)):
		if not taken[pair_with] and are_friends[first_student][pair_with]:
			taken[first_student] = taken[pair_with] = True
			# 재귀일 때, refernce 참조로 넘겨도 문제 없나 흐음...
			# 사람처럼 한 번에 일련의 과정을 전체 탐색하는 것이 아님으로,
			# 한 가지에 들어갔을 때 막고 풀면 문제 없음
			ret += count_pairing(are_friends, taken)
			taken[first_student] = taken[pair_with] = False
	return ret


def main():
	case_num = int(input())
	for _ in range(case_num):
		# 첫 번째는 학생 수, 두 번째는 친구 쌍의 수
		student, friend_num = tuple(map(int, input().split()))
		friend_list = list(map(int, input().split()))
		are_friends, taken = initiate(student, friend_num, friend_list)
		print(count_pairing(are_friends, taken))


def file_main():
	# file로 검사하기 위한 main
	file = open('5_test.txt', 'r', encoding='utf-8')
	case_num = int(file.readline())
	for _ in range(case_num):
		# 첫 번째는 학생 수, 두 번째는 친구 쌍의 수
		student, friend_num = tuple(map(int, file.readline().split()))
		friend_list = list(map(int, file.readline().split()))
		are_friends, taken = initiate(student, friend_num, friend_list)
		print(count_pairing(are_friends, taken))
	file.close()


if __name__ == '__main__':
	main()
