from typing import List


def check(nums: List[int]) -> bool:
    def Judge():
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                return False
        return True

    for _ in range(len(nums)):
        if Judge():
            return True
        Temp = nums.pop(0)
        nums.append(Temp)
    return False
