def mergeAlternately(word1: str, word2: str) -> str:
    Res = ''
    Index1, Index2 = 0, 0
    while Index1 < len(word1) and Index2 < len(word2):
        Res += word1[Index1]
        Res += word2[Index2]
        Index1 += 1
        Index2 += 1
    while Index1 < len(word1):
        Res += word1[Index1]
        Index1 += 1
    while Index2 < len(word2):
        Res += word2[Index2]
        Index2 += 1
    return Res
