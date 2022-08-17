from typing import List


def edgeScore(edges: List[int]) -> int:
    Score = [0] * len(edges)
    for idx, index in enumerate(edges):
        Score[index] += idx
    return Score.index(max(Score))