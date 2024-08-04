from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        arr = []
        for index in range(1, len(mountain) - 1):
            if mountain[index - 1] < mountain[index] and mountain[index + 1] < mountain[index]:
                arr.append(index)
        return arr
