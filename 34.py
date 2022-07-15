from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    Left, Right, Index = 0, len(nums) - 1, -1
    while Left <= Right:
        Mid = int((Left + Right) / 2)
        if nums[Mid] == target:
            Index = Mid
            break
        if nums[Mid] < target:
            Left = Mid + 1
        if nums[Mid] > target:
            Right = Mid - 1
    if Index == -1:
        return [-1, -1]
    else:
        IndexLeft = Index
        IndexRight = Index
        Res = []
        while IndexLeft >= 0 and nums[IndexLeft] == target:
            IndexLeft -= 1
        while IndexRight < len(nums) and nums[IndexRight] == target:
            IndexRight += 1
        if IndexLeft >= 0 and nums[IndexLeft] == target:
            Res.append(IndexLeft)
        else:
            Res.append(IndexLeft + 1)
        if IndexRight < len(nums) and nums[IndexRight] == target:
            Res.append(IndexRight)
        else:
            Res.append(IndexRight - 1)
        return Res


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([1], 1))
