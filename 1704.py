from collections import Counter


def halvesAreAlike(s: str) -> bool:
    Chars = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    Cnt1, Cnt2 = 0, 0
    for char in s[:len(s) // 2]:
        if char in Chars:
            Cnt1 += 1
    for char in s[len(s) // 2:]:
        if char in Chars:
            Cnt2 += 1
    return Cnt1 == Cnt2
