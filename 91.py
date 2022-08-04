def numDecodings(s: str) -> int:
    DP = [1] + [0] * len(s)
    for Index in range(1, len(s) + 1):
        if s[Index - 1] != '0':
            DP[Index] += DP[Index - 1]
        if Index > 1 and s[Index - 2] != "0" and int(s[Index - 2:Index]) < 27:
            DP[Index] += DP[Index - 2]
    return DP[len(s)]


if __name__ == "__main__":
    s = "226"
    print(numDecodings(s))
