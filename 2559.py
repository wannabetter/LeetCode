from typing import List


def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    def isVowel(word):
        return True if word in {"a", "e", "i", "o", "u"} else False

    def isVowelString(strs):
        return isVowel(strs[0]) and isVowel(strs[-1])

    n = len(words)
    prefix = [0] * (n + 1)
    for index in range(n):
        prefix[index + 1] = prefix[index] + (1 if isVowelString(words[index]) else 0)

    ans = []
    for start, end in queries:
        ans.append(prefix[end + 1] - prefix[start])
    return ans
