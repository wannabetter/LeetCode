from typing import List


def maxArea(height: List[int]) -> int:
    Left, Right = 0, len(height) - 1
    Res = -1
    while Left < Right:
        Res = max(min(height[Left], height[Right]) * (Right - Left), Res)
        if height[Left] < height[Right]:
            Left = Left + 1
        else:
            Right = Right - 1
    return Res