def squareIsWhite(coordinates: str) -> bool:
    Dicts = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    Row, Col = coordinates[0], coordinates[1]
    return not Dicts[Row] % 2 == int(Col) % 2
