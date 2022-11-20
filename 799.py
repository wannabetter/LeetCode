def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    Row = [poured]
    for Index in range(1, query_row + 1):
        nextRow = [0] * (Index + 1)
        for Idx, Val in enumerate(Row):
            if Val >= 1:
                nextRow[Idx] += (Val - 1) / 2
                nextRow[Idx + 1] += (Val - 1) / 2
        Row = nextRow
    return min(1, Row[query_glass])
