from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    Chars1, Chars2 = "", ""
    for word in word1:
        Chars1 += word
    for word in word2:
        Chars2 += word
    return Chars1 == Chars2