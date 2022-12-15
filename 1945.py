def getLucky(s: str, k: int) -> int:
    Res = ''
    for char in s:
        Res += str(ord(char) - ord('a'))
    while k:
        Temp = str(Res)
        Res = 0
        Res += sum(map(int, Temp))
        k -= 1
    return Res
