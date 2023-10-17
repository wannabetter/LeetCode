def sumOfMultiples(n: int) -> int:
    ans = 0
    for num in range(1, n + 1):
        if num % 3 == 0:
            ans += num
        elif num % 5 == 0:
            ans += num
        elif num % 7 == 0:
            ans += num
    return ans
