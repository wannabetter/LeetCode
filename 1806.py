def reinitializePermutation(n: int) -> int:
    prem = [idx for idx in range(n)]
    arr = [prem[index // 2] if index % 2 == 0 else prem[n // 2 + (index - 1) // 2] for index, val in enumerate(prem)]
    ans = 1
    while arr != prem:
        Temp = arr
        arr = [Temp[index // 2] if index % 2 == 0 else Temp[n // 2 + (index - 1) // 2] for index, val in
               enumerate(prem)]
        ans += 1
    return ans
