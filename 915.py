from typing import List


def partitionDisjoint(nums: List[int]) -> int:
    CurMax, LeftMax, LeftIndex = nums[0], nums[0], 0
    for Index in range(1, len(nums) - 1):
        CurMax = max(CurMax, nums[Index])
        if LeftMax > nums[Index]:
            LeftMax = CurMax
            LeftIndex = Index
    return LeftIndex + 1