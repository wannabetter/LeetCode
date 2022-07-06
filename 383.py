from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    cnt = Counter()
    for char in magazine:
        cnt[char] += 1
    for char in ransomNote:
        cnt[char] -= 1
        if cnt[char] < 0:
            return False
    return True
