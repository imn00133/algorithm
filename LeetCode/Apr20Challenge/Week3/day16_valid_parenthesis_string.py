# https://leetcode.com/problems/valid-parenthesis-string/
# Solved Date: 20.04.16.


def greed_valid_string(s):
    lo = hi = 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        if hi < 0:
            break
        lo = max(lo, 0)
    return lo == 0


def check_valid_string(s):
    stack = []
    asterisk = 0
    for letter in s:
        if letter == '(':
            if len(stack) < asterisk:
                asterisk -= 1
            stack.append(letter)
        elif letter == ')':
            if stack:
                stack.pop()
            elif asterisk > 0:
                asterisk -= 1
            else:
                return False
        else:
            asterisk += 1
    if not stack or len(stack) <= asterisk:
        return True
    else:
        return False


def main():
    s = input()
    print(greed_valid_string(s))
    print(check_valid_string(s))


if __name__ == '__main__':
    main()
