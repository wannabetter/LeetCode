from typing import List
from bisect import bisect_left
from collections import defaultdict


def numMatchingSubseq(s: str, words: List[str]) -> int:
    Res = 0
    Cnt = defaultdict(list)
    for index, char in enumerate(s):
        Cnt[char].append(index)
    for word in words:
        IndexI, IndexJ = 0, 0
        while IndexI < len(s) and IndexJ < len(word):
            if word[IndexJ] not in Cnt:
                break
            NextIndexI = bisect_left(Cnt[word[IndexJ]], IndexI)
            if NextIndexI == len(Cnt[word[IndexJ]]):
                break
            IndexI = Cnt[word[IndexJ]][NextIndexI] + 1
            IndexJ += 1
        if IndexJ == len(word):
            Res += 1
    return Res


if __name__ == '__main__':
    print(numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]))
