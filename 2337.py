def canChange(start: str, target: str) -> bool:
    n = len(start)
    index_i, index_j = 0, 0
    while index_i < n and index_j < n:
        while index_i < n and start[index_i] == "_":
            index_i = index_i + 1
        while index_j < n and target[index_j] == "_":
            index_j = index_j + 1
        if index_i < n and index_j < n:
            if start[index_i] != target[index_j]:
                return False
            c = start[index_i]
            if (c == "L" and index_i < index_j) or (c == "R" and index_i > index_j):
                return False
            index_i = index_i + 1
            index_j = index_j + 1
    while index_i < n:
        if start[index_i] != "_":
            return False
        index_i = index_i + 1
    while index_j < n:
        if target[index_j] != "_":
            return False
        index_j = index_j + 1
    return True