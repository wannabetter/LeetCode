from typing import List


def camelMatch(queries: List[str], pattern: str) -> List[bool]:
    res = []
    for query in queries:
        index1, index2 = 0, 0
        while index1 < len(query) and index2 < len(pattern):
            if query[index1] == pattern[index2]:
                index2 += 1
            else:
                if 'A' <= query[index1] <= 'Z':
                    break
            index1 += 1
        while index1 < len(query):
            if 'A' <= query[index1] <= 'Z':
                break
            index1 += 1
        res.append(True if index1 == len(query) and index2 == len(pattern) else False)
    return res
