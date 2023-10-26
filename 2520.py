def countDigits(num: int) -> int:
    ans = 0
    arr = list(str(num))
    for i in arr:
        if num % int(i) == 0:
            ans += 1
    return ans
