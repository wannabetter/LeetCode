def integerBreak(n: int) -> int:
    DP = [0] * (n + 1)

    for R in range(2, n + 1):
        for L in range(R):
            DP[R] = max(L * (R - L), L * DP[R - L], DP[R])
    print(DP)
    return max(DP)


if __name__ == "__main__":
    print(integerBreak(10))
