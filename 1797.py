class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenMap = set()
        self.hashMap = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenMap.add(tokenId)
        self.hashMap[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokenMap or (
                tokenId in self.tokenMap and self.hashMap[tokenId] + self.timeToLive <= currentTime):
            return
        self.hashMap[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for key, val in self.hashMap.items():
            if val + self.timeToLive > currentTime:
                ans += 1
        return ans
