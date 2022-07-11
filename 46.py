from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def BackTrace(index=0):
        if index == len(nums):
            res.append(nums[:])
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            BackTrace(index+1)
            nums[index], nums[i] = nums[i], nums[index]

    res = []
    BackTrace()
    return res
