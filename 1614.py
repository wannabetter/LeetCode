def maxDepth(s: str) -> int:
    Max, ans = 0, 0
    for i in s:
        if i == '(':
            ans = ans + 1
            Max = max(Max, ans)
        if i == ')':
            ans = ans - 1
    return Max
