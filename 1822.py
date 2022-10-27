def arraySign(nums: List[int]) -> int:
    Sum = 0
    for num in nums:
        if num < 0:
            Sum += 1
        if num == 0:
            return 0
    return (-1) ** Sum