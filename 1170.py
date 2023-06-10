from typing import List


def numSmallerByFrequency(queries: List[str], words: List[str]) -> List[int]:
    def f(word: str) -> int:
        ans = 0
        char = 'z'

        for c in word:
            if c < char:
                char = c
                ans = 1
            elif c == char:
                ans += 1
        return ans

    res = []

    for index, query in enumerate(queries):
        queries[index] = f(query)

    for index, word in enumerate(words):
        words[index] = f(word)

    for i in range(len(queries)):
        res.append(0)
        for j in range(len(words)):
            if queries[i] < words[j]:
                res[-1] += 1
    return res