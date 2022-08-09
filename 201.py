def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    while left < right:
        right = right >> 1
        left = left >> 1
        shift += 1
    return left << shift
