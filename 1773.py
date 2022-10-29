from typing import List


def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    Dicts = {"color": 1, "type": 0, "name": 2}
    ruleKey = Dicts[ruleKey]
    Sum = 0
    for item in items:
        if item[ruleKey] == ruleValue:
            Sum += 1
    return Sum
