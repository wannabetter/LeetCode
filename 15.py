from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    else:
        Res = []
        nums.sort()
        for Index, Num in enumerate(nums):
            if Index > 0 and nums[Index] == nums[Index - 1]:
                continue
            Left, Right = Index + 1, len(nums) - 1
            while Left < Right:
                Target = Num + nums[Left] + nums[Right]
                if Target == 0:
                    Res.append([Num, nums[Left], nums[Right]])
                    while Left < Right and nums[Left] == nums[Left + 1]:
                        Left = Left + 1
                    while Left < Right and nums[Right] == nums[Right - 1]:
                        Right = Right - 1
                    Right = Right - 1
                if Target > 0:
                    Right = Right - 1
                if Target < 0:
                    Left = Left + 1
        return Res


if __name__ == "__main__":
    print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
