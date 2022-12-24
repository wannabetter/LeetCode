def largestMerge(word1: str, word2: str) -> str:
    Res = ''
    word1, word2 = list(word1), list(word2)
    while len(word1) and len(word2):
        if word1 > word2:
            Res += word1.pop(0)
        else:
            Res += word2.pop(0)
    while len(word1):
        Res += word1.pop(0)
    while len(word2):
        Res += word2.pop(0)
    return Res
