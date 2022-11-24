from typing import List


def numSubarrayBoundedMax(nums: List[int], left: int, right: int) -> int:
    Res, Stack, Left, Right = 0, [], [-1] * len(nums), [len(nums)] * len(nums)
    for Index in range(len(nums)):
        while Stack and nums[Stack[-1]] < nums[Index]:
            Right[Stack.pop()] = Index
        Stack.append(Index)
    Stack = []
    for Index in range(len(nums) - 1, -1, -1):
        while Stack and Stack[nums[-1]] <= nums[Index]:
            Left[Stack.pop()] = Index
        Stack.append(Index)
    for Index in range(len(nums)):
        if left <= nums[Index] <= right:
            Res += (Index - Left[Index]) * (Right[Index] - Index)
    return Res
