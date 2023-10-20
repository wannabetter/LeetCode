def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    Bulky, Heavy = 0, 0
    if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or mass >= 10 ** 4 or length * width * height >= 10 ** 9:
        Bulky = 1
    if mass >= 100:
        Heavy = 1
    if Bulky and Heavy:
        return 'Both'
    elif Bulky:
        return 'Bulky'
    elif Heavy:
        return 'Heavy'
    else:
        return 'Neither'
