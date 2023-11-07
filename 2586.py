from typing import List


def vowelStrings(words: List[str], left: int, right: int) -> int:
    ans = 0
    flags = ['a', 'e', 'i', 'o', 'u']
    while left <= right:
        if words[left][0] in flags and words[left][-1] in flags:
            ans += 1
        left += 1
    return ans
