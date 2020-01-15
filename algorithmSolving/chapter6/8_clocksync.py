# Solving Date: 20.01.02.
# Site: https://algospot.com/judge/problem/read/CLOCKSYNC
# 본 풀이는 시간초과가 난다.

# INF는 어느정도로 잡아야되나 -> 스위치당 4개쓱 묵여있으니, 단순하게 4^4정도가 최대인가.
INF, SWITCHSNUM, CLOCKSNUM = 9999, 10, 16
# linked[i][j] = x: i번 스위치와 j번 시계가 연결되어 있다.
# linked[i][j] = .: i번 스위치와 j번 시계까 연결되어있지 않다.
# True와 False로 만들려고 하였으나, 개수가 헷갈림
# 고정 글꼴임으로 .과 x의 크기가 같다는 점으로 보기 쉽게 만들 수 있다.
linked = [
	# 0123456789012345
	"xxx.............",
	"...x...x.x.x....",
	"....x.....x...xx",
	"x...xxxx........",
	"......xxx.x.x...",
	"x.x...........xx",
	"...x..........xx",
	"....xx.x......xx",
	".xxxxx..........",
	"...xxx...x...x.."
]


def are_aligned(clock_list):
	# clock_list 내부상태가 12인지 확인한다.
	for state in clock_list:
		if state != 12:
			return False
	return True


def push(clock_list, switch):
	# switch번 스위치 눌러 시계 변겅하기
	# magic number는 안쓰는 것이 좋겠지만, 알고리즘 문제가 바뀔일은 없으니까...
	for clock in range(CLOCKSNUM):
		if linked[switch][clock] == 'x':
			clock_list[clock] += 3
			if clock_list[clock] == 15:
				clock_list[clock] = 3


def solve(clock_list, switch):
	# clock_list: 현재 시계들의 상태 목록
	# switch: 이번에 누를 스위치의 번호
	# 남은 스위치를 눌러서 clock_list를 12시로 맞출 수 있는 최소 횟수 반환
	# 불가능 하면 INF이상의 큰 수를 반환
	if switch == SWITCHSNUM:
		# 삼항 연산자 참일때 출력 if 조건 else 거짓일 때 출력
		return 0 if are_aligned(clock_list) else INF
	ret = INF
	# 스위치를 0번-3번 누르는 걸 전부 테스트
	for cnt in range(4):
		ret = min(ret, cnt + solve(clock_list, switch+1))
		push(clock_list, switch)
	return ret


def main():
	case_num = int(input())
	for _ in range(case_num):
		clock_list = list(map(int, input().split()))
		value = solve(clock_list, 0)
		if value < INF:
			print(value)
		else:
			print(-1)


def file_main():
	file = open('8_test.txt', 'r', encoding='utf-8')
	case_num = int(file.readline())
	for _ in range(case_num):
		clock_list = list(map(int, file.readline().split()))
		value = solve(clock_list, 0)
		if value < INF:
			print(value)
		else:
			print(-1)


if __name__ == '__main__':
	main()
