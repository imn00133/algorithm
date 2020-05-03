# https://leetcode.com/problems/ransom-note/
# Solved Date: 20.05.03.


def can_construct(ransomNote, magazine):
    from collections import Counter
    magazine_counter = Counter(magazine)
    ransomNote_counter = Counter(ransomNote)
    for letter in ransomNote_counter.keys():
        if magazine_counter[letter] < ransomNote_counter[letter]:
            return False
    return True
