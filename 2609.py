def findTheLongestBalancedSubstring(s: str) -> int:
    ans = 0
    index = 0
    while index < len(s):
        zero, one = 0, 0
        while index < len(s) and s[index] == "0":
            zero = zero + 1
            index = index + 1
        while index < len(s) and s[index] == "1":
            one = one + 1
            index = index + 1
        ans = max(ans, one * 2 if zero >= one else zero * 2)
    return ans