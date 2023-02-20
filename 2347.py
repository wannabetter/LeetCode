from typing import List
from collections import Counter


def bestHand(ranks: List[int], suits: List[str]) -> str:
    ranksCnt, suitsCnt = Counter(ranks), Counter(suits)
    if any(val == 5 for val in suitsCnt.values()):
        return "Flush"
    elif any(val >= 3 for val in ranksCnt.values()):
        return "Three of a Kind"
    elif any(val == 2 for val in ranksCnt.values()):
        return "Pair"
    else:
        return "High Card"
