import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.newList = nums.copy()
        self.shuffleList = nums

    def reset(self) -> List[int]:
        return self.newList

    def shuffle(self) -> List[int]:
        shuffled = [0] * len(self.shuffleList)
        for i in range(len(self.shuffleList)):
            j = random.randrange(len(self.shuffleList))
            shuffled[i] = self.shuffleList.pop(j)
        self.shuffleList = shuffled
        return self.shuffleList
