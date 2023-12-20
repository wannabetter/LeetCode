from typing import List


def isAcronym(words: List[str], s: str) -> bool:
    ans = ""
    for word in words:
        ans = ans + word[0]
    return ans == s