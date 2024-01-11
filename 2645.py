from itertools import pairwise


def addMinimum(word: str) -> int:
    ans = ord(word[0]) - ord(word[-1]) + 2
    for x, y in pairwise(map(ord, word)):
        ans = ans + (y - x + 2) % 3
    return ans
