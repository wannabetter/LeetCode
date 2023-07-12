def alternateDigitSum(n: int) -> int:
    ans = 0
    strs = str(n)
    for index, c in enumerate(strs):
        if index % 2 == 0:
            ans += int(c)
        else:
            ans -= int(c)
    return ans
