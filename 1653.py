def minimumDeletions(s: str) -> int:
    res = len(s)
    leftB, rightA = 0, s.count('a')
    for char in s:
        rightA -= char == 'a'
        res = min(res, leftB + rightA)
        leftB += char == 'b'
    return res
