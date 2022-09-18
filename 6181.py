def longestContinuousSubstring(s: str) -> int:
    DP = [1] * len(s)
    for index in range(1, len(s)):
        if ord(s[index]) - ord(s[index - 1]) == 1:
            DP[index] = DP[index-1] + 1
        else:
            DP[index] = 1
    print(DP)
    return max(DP)


if __name__ == '__main__':
    print(longestContinuousSubstring("abcde"))
