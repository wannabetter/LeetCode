def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    index1, index2 = 0, 0
    word1, word2 = sentence1.split(), sentence2.split()
    while index1 < len(word1) and index1 < len(word2) and word1[index1] == word2[index1]:
        index1 += 1
    while index2 < len(word1) - index1 and index2 < len(word2) - index1 and word2[-(index2 + 1)] == word1[
        -(index2 + 1)]:
        index2 += 1
    return index2 + index1 == min(len(word1), len(word2))
