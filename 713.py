from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    else:
        Start, End, Res, Total = 0, 0, 0, 1
        while End < len(nums):
            Total = Total * nums[End]
            while Start < len(nums) and Total >= k:
                Total = Total / nums[Start]
                Start = Start + 1
            Res += End - Start + 1  # 加上X总组合数，这个地方是最关键的！
            End = End + 1
        return Res
