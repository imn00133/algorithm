# https://www.acmicpc.net/problem/14391
# Solved Date: 20.04.19.

import sys
read = sys.stdin.readline


def baekjoon(n, m, a):
    ans = 0
    for s in range(1 << (n * m)):
        sum = 0
        for i in range(n):
            cur = 0
            for j in range(m):
                k = i * m + j
                if (s & (1 << k)) == 0:
                    cur = cur * 10 + a[i][j]
                else:
                    sum += cur
                    cur = 0
            sum += cur
        for j in range(m):
            cur = 0
            for i in range(n):
                k = i * m + j
                if (s & (1 << k)) != 0:
                    cur = cur * 10 + a[i][j]
                else:
                    sum += cur
                    cur = 0
            sum += cur
        ans = max(ans, sum)
    return ans


def bit_mask(row, col, paper):
    max_score = 0
    arr_size = row * col
    for index in range(1 << arr_size):
        score = 0
        for y in range(row):
            number = 0
            for x in range(col):
                k = y * row + x
                if index & (1 << k):
                    number = number * 10 + paper[y][x]
                else:
                    score += number
                    number = 0
            score += number
        for x in range(col):
            number = 0
            for y in range(row):
                k = y * row + x
                if index & (1 << k) == 0:
                    number = number * 10 + paper[y][x]
                else:
                    score += number
                    number = 0
            score += number
        max_score = max(max_score, score)
    return max_score


def main():
    row, col = (int(x) for x in read().split())
    paper = []
    for _ in range(row):
        paper.append([int(x) for x in list(read().strip())])
    print(bit_mask(row, col, paper))


def test():
    for row in range(1, 4):
        for col in range(1, 4):
            print("row: {}, col: {} 실험 시작".format(row, col))
            total_count = row * col
            for value in range(10 ** total_count):
                value_str = str(value)
                temp = [0 for _ in range(row * col - len(value_str))]
                temp.extend([int(x) for x in value_str])
                paper = []
                index = 0
                next_index = col
                for _ in range(row):
                    paper.append(temp[index:next_index])
                    index = next_index
                    next_index += col
                expect = baekjoon(row, col, paper)
                real = bit_mask(row, col, paper)
                if expect != real:
                    print(paper)
                    print("expect: {}".format(expect))
                    print("real: {}".format(real))
                if total_count >= 5 and value % 10000 == 0:
                    print("{:0}퍼센트 진행".format(value / (10 ** total_count) * 100))
            print("row: {}, col: {} 실험 종료".format(row, col))


if __name__ == '__main__':
    test()
    main()
