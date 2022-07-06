def lengthOfLongestSubstring(s: str) -> int:
    occ = set()
    rk, ans = -1, 0
    for item in range(len(s)):
        if item != 0:
            occ.remove(s[item - 1])
        while rk + 1 < len(s) and s[rk + 1] not in occ:
            occ.add(s[rk + 1])
            rk += 1
        ans = max(ans, rk - item + 1)
    return ans
