def canTransform(start: str, end: str) -> bool:
    IndexS, IndexE, Start, End = 0, 0, list(start), list(end)
    while IndexS < len(start) or IndexE < len(end):
        while IndexS < len(start) and Start[IndexS] == "X":
            IndexS += 1
        while IndexE < len(end) and End[IndexE] == "X":
            IndexE += 1
        if IndexS == len(start) or IndexE == len(end):
            return IndexS == IndexE
        if Start[IndexS] != End[IndexE]:
            return False
        if Start[IndexS] == "L" and IndexS < IndexE:
            return False
        if Start[IndexS] == "R" and IndexS > IndexE:
            return False
        IndexS += 1
        IndexE += 1
    return IndexS == IndexE
