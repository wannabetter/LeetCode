def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    if k <= numOnes:
        return k
    else:
        k = k - numOnes
    if k <= numZeros:
        return numOnes
    else:
        k = k - numZeros
    if k <= numNegOnes:
        return numOnes - k
