# https://leetcode.com/problems/valid-parenthesis-string/
# Solved Date: 20.04.16.


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
    print(check_valid_string(s))


if __name__ == '__main__':
    main()
