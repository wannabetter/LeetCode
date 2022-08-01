from typing import List


def rob(nums: List[int]) -> int:
    def RobStartEnd(Start, End):
        Front, Rear = nums[Start], max(nums[Start], nums[Start + 1])
        for Index in range(Start + 2, End + 1):
            Front, Rear = Rear, max(Front + nums[Index], Rear)
        return Rear

    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[0])
    else:
        return max(RobStartEnd(0, len(nums) - 2), RobStartEnd(1, len(nums) - 1))


if __name__ == "__main__":
    print(rob([2, 3, 2]))
