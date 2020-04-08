# https://leetcode.com/problems/group-anagrams
# Solved Date: 20.04.06.
# solution 참고함


def use_default_dict(strs):
    import collections
    ans = collections.defaultdict(list)
    for i in strs:
        ans[tuple(sorted(i))].append(i)
    return ans.values()


def fast_anagrams(strs):
    anagrams_dict = {}
    for string in strs:
        # 다른 방법으로는 ascii tuple을 만들어서 저장한다.
        sort_str = tuple(sorted(string))
        if sort_str in anagrams_dict:
            anagrams_dict[sort_str].append(string)
        else:
            anagrams_dict[sort_str] = [string]
    return list(anagrams_dict.values())


def group_anagrams(strs):
    # 시간초과
    anagrams_strs = []
    overlap_check = []
    for string in strs:
        flag_exist = False
        str_dict = {}
        for letter in string:
            if letter in str_dict:
                str_dict[letter] += 1
            else:
                str_dict[letter] = 1
        dict_items = sorted(list(str_dict.items()))
        for index, overlap_dict in enumerate(overlap_check):
            overlap_dict_items = sorted(list(overlap_dict.items()))
            if dict_items == overlap_dict_items:
                anagrams_strs[index].append(string)
                flag_exist = True
                break
        if not flag_exist:
            anagrams_strs.append([string])
            overlap_check.append(str_dict)
    return anagrams_strs


def main():
    strs = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
    print(group_anagrams(strs))


if __name__ == '__main__':
    main()
