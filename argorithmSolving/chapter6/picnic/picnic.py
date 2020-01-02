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
	# 기저 사례: 모든 학생이 짝을 찾으면 한 가지 방법을 찾아서 종료
	if all(taken):
		return 1
	ret = 0
	# 같은 학생 짝 두 번 짓는 것, 다른 순서로 학생들을 짝짓는 것을 해소해야함
	# 두 번째 검사의 시작을 i 이후로 잡으면 다른 순서로 학생을 짝 짓는 것이 포함됨
	for i in range(len(taken)):
		for j in range(i, len(taken)):
			if not taken[i] and not taken[j] and are_friends[i][j]:
				taken[i] = taken[j] = True
				# 재귀일 때, refernce 참조로 넘겨도 문제 없나 흐음...
				ret += count_pairing(are_friends, taken)
				taken[i] = taken[j] = False
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
	file = open('test.txt', 'r', encoding='utf-8')
	case_num = int(file.readline())
	for _ in range(case_num):
		# 첫 번째는 학생 수, 두 번째는 친구 쌍의 수
		student, friend_num = tuple(map(int, file.readline().split()))
		friend_list = list(map(int, file.readline().split()))
		are_friends, taken = initiate(student, friend_num, friend_list)
		print(count_pairing(are_friends, taken))
	file.close()


if __name__ == '__main__':
	file_main()
