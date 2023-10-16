from typing import List


def singleNumber(nums: List[int]) -> List[int]:
    xor = 0
    for num in nums:
        xor ^= num
    lab = xor & (-xor)
    num1,num2=0,0
    for num in nums:
        if lab & num:
            num1 ^= num
        else:
            num2 ^= num
    return [num1,num2]