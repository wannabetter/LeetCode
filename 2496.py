def maximumValue(strs: List[str]) -> int:
    ans = 0
    for item in strs:
        if item.isdigit():
            ans = max(ans, int(item))
        else:
            ans = max(ans, len(item))
    return ans
