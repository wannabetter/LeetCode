from typing import List


def expressiveWords(s: str, words: List[str]) -> int:
    def Expand(Chars1, Chars2):
        Index1, Index2 = 0, 0
        while Index1 < len(Chars1) and Index2 < len(Chars2):
            if Chars1[Index1] != Chars2[Index2]:
                return False
            Cnt1, Cnt2 = 0, 0
            Char = Chars1[Index1]
            while Index1 < len(Chars1) and Chars1[Index1] == Char:
                Cnt1 += 1
                Index1 += 1
            while Index2 < len(Chars2) and Chars2[Index2] == Char:
                Cnt2 += 1
                Index2 += 1

            if Cnt1 < Cnt2:
                return False

            if Cnt1 != Cnt2 and Cnt1 < 3:
                return False
        return Index1 == len(Chars1) or Index2 == len(Chars2)

    return sum(Expand(s, word) for word in words)
