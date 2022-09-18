from typing import List
from collections import Counter


def sumPrefixScores(words: List[str]) -> List[int]:
    Res = []
    Cnt = Counter()

    for word in words:
        Chars = ""
        for char in word:
            Chars += char
            Cnt[Chars] += 1

    for word in words:
        Len = 0
        Chars = ""
        for char in word:
            Chars += char
            Len += Cnt[Chars]
        Res.append(Len)
    return Res
