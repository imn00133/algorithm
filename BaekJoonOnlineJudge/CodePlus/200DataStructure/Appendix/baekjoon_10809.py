# https://www.acmicpc.net/problem/10809
# Solving Date: 20.03.28.
# https://wookiist.tistory.com/29 알파벳 리스트 만들기
# pythonic한 것이 두 배 느리다(112ms/60ms) 아마 string을 import하는게 무거운게 아닐까 싶다.


def solve_ascii(string):
    index_ascii = [-1 for x in range(ord('z')-ord('a')+1)]
    for index, letter in enumerate(string):
        ascii_index = ord(letter) - ord('a')
        if index_ascii[ascii_index] == -1:
            index_ascii[ascii_index] = index
    return index_ascii


def solve_pythonic(ref_string):
    import string
    index_ascii = []
    for alphabet in string.ascii_lowercase:
        index_ascii.append(ref_string.find(alphabet))
    return index_ascii


def main():
    string = input()
    index_ascii = solve_ascii(string)
    for value in index_ascii:
        print(value, end=' ')


if __name__ == "__main__":
    main()
