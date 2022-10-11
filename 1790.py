def areAlmostEqual(s1: str, s2: str) -> bool:
    n = len(s1)
    Index = 0
    Sum = 0
    while Index < n:
        if s1[Index] != s2[Index]:
            Sum += 1
        Index += 1
    return (Sum == 2 or Sum == 0) and (Counter(s1) == Counter(s2))
