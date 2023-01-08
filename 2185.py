from typing import List


def prefixCount(words: List[str], pref: str) -> int:
    Res, n = 0, len(pref)
    for word in words:
        if word[:n] == pref:
            Res += 1
    return Res
