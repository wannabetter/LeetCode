def kthGrammar(n: int, k: int) -> int:
    if k == 1:
        return 0
    if k <= 2 ** (n - 2):
        return kthGrammar(n - 1, k)
    else:
        return 1 ^ kthGrammar(n - 1, k - 2 ** (n - 2))
