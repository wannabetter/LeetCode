import math


class Solution:
    def isPrime(self, n: int) -> int:
        if n == 1:
            return 0
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return 0
            return 1

    def fac(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            res = res * i
            res = res % (10 ** 9 + 7)
        return res

    def numPrimeArrangements(self, n: int) -> int:
        numPrime = sum(self.isPrime(i) for i in range(1, n + 1))
        Sum = self.fac(numPrime) * self.fac(n - numPrime) % (10 ** 9 + 7)
        return Sum
