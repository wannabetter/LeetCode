from typing import List


def maxProduct(nums: List[int]) -> int:
    Temp=[]
    for num in nums:
        if len(Temp)<2:
            Temp.append(num)
        else:
            if min(Temp) < num:
                Temp.remove(min(Temp))
                Temp.append(num)
    return (Temp[0]-1)*(Temp[1]-1)
