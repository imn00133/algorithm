# Solving Date: 20.01.18.
# site: https://algospot.com/judge/problem/read/BOGGLE
# 본 풀이는 완전 탐색을 사용함으로, 시간초과가 난다.

# DX, DY: 상대적 위치를 표현 상수
# BOARDWITH, BOARDHEIGHT: 보드판의 크기 지정 상수
# 매직넘버는 제거하는 것이 좋다.
DX = (-1, -1, -1, 1, 1, 1, 0, 0)
DY = (-1, 0, 1, -1, 0, 1, -1, 1)
BOARDWIDTH = 5
BOARDHEIGHT = 5


def in_range(y, x):
	return 0 <= y < BOARDHEIGHT and 0 <= x < BOARDWIDTH


def has_word(y, x, board, word):
	# 5x5의 보글 게임 판의 해당위치에서 주어진 단어가 시작하는지 확인하여 반환
	# 기저사례 1: 시작 위치가 범위 밖이면 무조건 실패
	if not in_range(y, x):
		return False
	# 기저사례 2: 첫 글자가 일치하지 않으면 실패
	if board[y][x] != word[0]:
		return False
	# 기저 사례 3: 단어 길이가 1이면 성공
	# 기저사례 2에서 첫 글자가 일치하지 않으면 return됨
	if len(word) == 1:
		return True
	for direction in range(8):
		next_y = y + DY[direction]
		next_x = x + DX[direction]
		if has_word(next_y, next_x, board, word[1:]):
			return True
	return False


def board_check(board, word):
	# 전체를 돌 수 있게 하는 함수
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			if has_word(y, x, board, word):
				return True
	return False


def main():
	case_num = int(input())
	for _ in range(case_num):
		board = []
		for _ in range(BOARDHEIGHT):
			board.append(input().strip())
		word_num = int(input())
		for _ in range(word_num):
			word = input()
			if board_check(board, word):
				print(word, "YES")
			else:
				print(word, "NO")


def file_main():
	file = open('2_test.txt', 'r', encoding='utf-8')
	case_num = int(file.readline())
	for _ in range(case_num):
		board = []
		for _ in range(BOARDHEIGHT):
			board.append(file.readline().strip())
		word_num = int(file.readline())
		for _ in range(word_num):
			# 파일로 받을 때, 개행문자는 항상 주의한다.
			word = file.readline().strip()
			if board_check(board, word):
				print(word, "YES")
			else:
				print(word, "NO")


if __name__ == '__main__':
	main()
