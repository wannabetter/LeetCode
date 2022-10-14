def distinctSubseqII(s: str) -> int:
    Chars = [0] * 26
    DP = [1] + [0] * len(s)
    for Index, Char in enumerate(s):
        DP[Index + 1] = DP[Index] * 2 - Chars[ord(Char) - ord("a")]
        Chars[ord(Char) - ord('a')] = DP[Index]
    return DP[-1] % (10 ** 9 + 7) - 1
