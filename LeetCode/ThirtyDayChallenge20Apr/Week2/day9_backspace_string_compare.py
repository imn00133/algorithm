# https://leetcode.com/problems/backspace-string-compare/
# Solved Date: 20.04.10.


def backspace_compare(S, T):
    stack_s = []
    stack_t = []
    for letter in S:
        if letter == '#':
            if stack_s:
                stack_s.pop()
        else:
            stack_s.append(letter)
    for letter in T:
        if letter == '#':
            if stack_t:
                stack_t.pop()
        else:
            stack_t.append(letter)
    if stack_s == stack_t:
        return True
    else:
        return False


def main():
    S = input()
    T = input()
    print(backspace_compare(S, T))


if __name__ == '__main__':
    main()
