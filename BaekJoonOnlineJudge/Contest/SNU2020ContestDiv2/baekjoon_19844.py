import sys

read = sys.stdin.readline
VOWELS = ('a', 'e', 'i', 'o', 'u', 'h')
START_WORD = ("c", "j", "n", "m", "t", "s", "l", "d")
CHECK = (' ', '-')


def count_words(sentence):
    count = 1
    stack = []
    for index in range(len(sentence)):
        letter = sentence[index]
        if letter in CHECK:
            count += 1
            stack.clear()
            continue
        elif letter == '\'' and sentence[index+1] in VOWELS:
            prev_letter = stack.pop()
            if not stack and prev_letter in START_WORD:
                count += 1
            elif prev_letter == 'u' and len(stack) == 1 and stack[-1] == 'q':
                count += 1
            stack.append(prev_letter)
        stack.append(letter)
    return count


def main():
    sentence = read()
    print(count_words(sentence))


if __name__ == "__main__":
    main()
