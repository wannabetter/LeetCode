from typing import List


def finalPrices(prices: List[int]) -> List[int]:
    Res = []
    for indexI in range(len(prices)):
        flag=True
        for indexJ in range(indexI + 1, len(prices)):
            if prices[indexJ] <= prices[indexI]:
                flag=False
                Res.append(prices[indexI] - prices[indexJ])
                break
        if flag:
            Res.append(prices[indexI])
    return Res


if __name__ == '__main__':
    print(finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]))
