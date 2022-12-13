def checkIfPangram(sentence: str) -> bool:
    Hash = set()
    for char in sentence:
        if 'a' <= char <= 'z':
            Hash.add(char)
    return len(Hash) == 26
