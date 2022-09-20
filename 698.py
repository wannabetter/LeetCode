from typing import List


def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    Sum = sum(nums)
    if Sum % k != 0:
        return False
    Index = 0
    Target = Sum // k
    nums.sort(reverse=True)
    if nums[0] > Target:
        return False
    while Index < len(nums) and nums[Index] == Target:
        Index += 1
        k -= 1
    SubSets = [0] * k

    def BackTrace(Idx):
        if Idx == len(nums):
            return True
        for i in range(k):
            if SubSets[i] + nums[Idx] <= Target:
                if i > 0 and SubSets[i - 1] + nums[Idx] == SubSets[i] + nums[Idx]:
                    continue
                SubSets[i] += nums[Idx]
                if BackTrace(Idx + 1):
                    return True
                SubSets[i] -= nums[Idx]
        return False

    return BackTrace(Index)
