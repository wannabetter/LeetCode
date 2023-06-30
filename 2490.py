def isCircularSentence(sentence: str) -> bool:
    sentences = list(sentence.split())
    if sentences[0][0] != sentences[-1][-1]:
        return False
    for index in range(1, len(sentences)):
        if sentences[index][0] != sentences[index - 1][-1]:
            return False
    return True
