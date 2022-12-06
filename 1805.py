from collections import Counter


def numDifferentIntegers(word: str) -> int:
    Index, Cnt = 0, Counter()
    while Index < len(word):
        Temp = ''
        while Index < len(word) and '0' <= word[Index] <= '9':
            Temp += word[Index]
            Index += 1
        if len(Temp) != 0:
            Cnt[int(Temp)] += 1
        Index += 1
    return len(Cnt)
