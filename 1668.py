def maxRepeating(sequence: str, word: str) -> int:
    Index, Max, LenSeq, LenWord = 0, 0, len(sequence), len(word)
    while Index < LenSeq:
        Sum = 0
        while Index + LenWord < LenSeq and sequence[Index:Index + LenWord] == word:
            Sum += 1
            Index += LenWord
        Max = max(Max, Sum)
        Index += 1
    return Max
