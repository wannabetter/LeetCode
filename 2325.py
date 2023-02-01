def decodeMessage(key: str, message: str) -> str:
    index = 0
    flags = set()
    dicts = dict()
    for char in key:
        if char == " ":
            continue
        if char not in flags:
            flags.add(char)
            dicts[char] = chr(ord('a') + index)
            index += 1

    ans = ""
    for mes in message:
        if mes == " ":
            ans += mes
        else:
            ans += dicts[mes]
    return ans
