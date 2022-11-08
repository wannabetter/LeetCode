from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    Dicts, Sum, Flag = set(allowed), 0, True
    for word in words:
        Flag = True
        for c in word:
            if c not in Dicts:
                Flag = False
        if Flag:
            Sum += 1
    return Sum
