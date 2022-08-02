from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    DP = [float('inf')] * (amount + 1)
    DP[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            DP[x] = min(DP[x], DP[x - coin] + 1)
    return DP[amount] if DP[amount] != float('inf') else -1


if __name__ == "__main__":
    print(coinChange(coins=[1, 2, 5], amount=11))
