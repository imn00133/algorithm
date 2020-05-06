# https://leetcode.com/problems/first-unique-character-in-a-string
# Solved Date: 20.05.06.


def first_unique_char_counter(s):
    from collections import Counter
    letter_dict = Counter(s)
    for index, letter in enumerate(s):
        if letter_dict[letter] == 1:
            return index
    return -1


def first_unique_char(s):
    from collections import defaultdict
    letter_dict = defaultdict(int)
    for letter in s:
        letter_dict[letter] += 1
    for index in range(len(s)):
        if letter_dict[s[index]] == 1:
            return index
    return -1
