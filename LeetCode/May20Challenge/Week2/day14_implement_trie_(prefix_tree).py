# https://leetcode.com/problems/implement-trie-prefix-tree/
# Solved Date: 20.05.15.


class DictTrie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        search_pos = self.root
        for letter in word:
            if letter not in search_pos:
                search_pos[letter] = {}
            search_pos = search_pos[letter]
        search_pos['!'] = True

    def search(self, word: str) -> bool:
        search_pos = self.root
        for letter in word:
            if letter not in search_pos:
                return False
            search_pos = search_pos[letter]
        return '!' in search_pos

    def starts_with(self, prefix: str) -> bool:
        search_pos = self.root
        for letter in prefix:
            if letter not in search_pos:
                return False
            search_pos = search_pos[letter]
        return True


class ArrayTrie:
    def __init__(self):
        self.start = ord('a')
        self.is_end = ord('{') - ord('a')
        self.links = [None for _ in range(self.is_end + 1)]

    def insert(self, word):
        search_pos = self.links
        for letter in word:
            letter = ord(letter) - self.start
            if search_pos[letter] is None:
                search_pos[letter] = [None for _ in range(self.is_end + 1)]
            search_pos = search_pos[letter]
        search_pos[self.is_end] = True

    def search(self, word):
        search_pos = self.links
        for letter in word:
            letter = ord(letter) - self.start
            if not search_pos[letter]:
                return False
            search_pos = search_pos[letter]
        return search_pos[self.is_end] is not None

    def startsWith(self, prefix):
        search_pos = self.links
        for letter in prefix:
            letter = ord(letter) - self.start
            if search_pos[letter] is None:
                return False
            search_pos = search_pos[letter]
        return True


def main():
    start = ArrayTrie()
    start.insert('apple')
    start.search('apple')
    start.search('app')
    start.startsWith('app')
    start.insert('app')
    start.search('app')


if __name__ == '__main__':
    main()
