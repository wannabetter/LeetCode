from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    ans = []
    ids = sorted([i for i in range(len(potions))], key=lambda i: potions[i])
    for spell in spells:
        left, right = 0, len(potions) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if potions[ids[mid]] * spell < success:
                left = mid
            else:
                right = mid - 1
        if potions[ids[left]] * spell >= success:
            ans.append(len(potions) - left)
        else:
            ans.append(len(potions) - left - 1)
    return ans
