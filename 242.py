from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    cnt = Counter()
    if len(s) > len(t):
        s, t = t, s
    for char in s:
        cnt[char] += 1
    for char in t:
        cnt[char] -= 1
        if cnt[char] < 0:
            return False
    return True
