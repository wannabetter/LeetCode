from typing import List
from collections import Counter


def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
    res = 0
    lettersCnt = Counter(letters)

    def DFS(index=0, total=0):
        if index == len(words):
            nonlocal res
            res = max(total, res)
            return

        DFS(index + 1, total)

        for idx, char in enumerate(words[index]):
            if lettersCnt[char] == 0:
                for backChar in words[index][:idx]:
                    lettersCnt[backChar] += 1
                return
            lettersCnt[char] -= 1
            total += score[ord(char) - ord('a')]

        DFS(index + 1, total)

        for char in words[index]:
            lettersCnt[char] += 1

    DFS()
    return res
