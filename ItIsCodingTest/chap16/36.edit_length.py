# 16 다이나믹 프로그래밍 - 편집 거리
# Solved Date: 22.07.03.
import sys
read = sys.stdin.readline


# 가장 긴 공통 문자열 찾기
# 추가, 삭제, 교체를 해서 편집함으로, 문자열 최대 길이에서 공통 문자열을 빼면 값이 나옴
# https://chanhuiseok.github.io/posts/algo-34/
def dynamic_programming(text1, text2):
    # dp[y][x] = text1의 y index, text2의 x index 까지 가장 긴 공통 문자열
    dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
    for y, letter1 in enumerate(text1, 1):
        for x, letter2 in enumerate(text2, 1):
            if letter1 == letter2:
                dp[y][x] = dp[y-1][x-1] + 1
                continue
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])
    return max(len(text1), len(text2)) - max(dp[-1])


def main():
    text1 = read().rstrip()
    text2 = read().rstrip()
    print(dynamic_programming(text1, text2))


if __name__ == '__main__':
    main()
