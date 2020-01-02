# Solving Date:
# site: https://algospot.com/judge/problem/read/BOARDCOVER

# 주어진 칸을 덮는 네 가지 방법
# COVERTYPE: 블럭을 구성하는 세 칸의 상대적 위치 (dx, dy)의 목록
COVERTYPE = (
	((0, 0), (1, 0), (0, 1)),
	((0, 0), (1, 0), (1, 1)),
	((0, 0), (0, 1), (1, 1)),
	((0, 0), (0, 1), (-1, 1))
)


def set_cover(board, x, y, cover_type, delta):
	pass


def main():
	case_num = int(input())
	for _ in range(case_num):
		height, width = tuple(map(int, input().split()))
		board = []
		for _ in range(height):
			temp_line = ' '.join(input()).split()
			for i in range(width):
				if temp_line[i] == '#':
					temp_line[i] = True
				else:
					temp_line[i] = False
			board.append(temp_line)


def file_main():
	file = open('5_test.txt', 'r', encoding='utf-8')
	case_num = int(file.readline())
	for _ in range(case_num):
		height, width = tuple(map(int, file.readline().split()))
		board = []
		for _ in range(height):
			temp_line = ' '.join(file.readline()).split()
			for i in range(width):
				if temp_line[i] == '#':
					temp_line[i] = True
				else:
					temp_line[i] = False
			board.append(temp_line)
	file.close()


if __name__ == '__main__':
	file_main()
