def queryString(s: str, n: int) -> bool:
    seen = set()
    s = list(map(int, s))

    for index, x in enumerate(s):
        if x == 0:
            continue
        j = index + 1
        while x <= n:
            if x not in seen:
                seen.add(x)
            if j == len(s):
                break
            x = (x << 1) | s[j]
            j += 1
    return len(seen) == n
