from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    cnt = Counter(s1)
    n = len(s1)
    index = 0
    while index <= len(s2) - n:
        if cnt[s2[index]] != 0:
            cnt2 = Counter(s2[index:index + n])
            if cnt2 == cnt:
                return True
        index = index + 1
    return False

