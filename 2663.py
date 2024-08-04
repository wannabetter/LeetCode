class Solution:
    def generate(self, s: str, idx: int, offset: int) -> str:
        res = list(s)
        res[idx] = chr(ord(res[idx]) + offset)
        for i in range(idx + 1, len(s)):
            blockedCharacters = set()
            for j in range(1, 3):
                if i - j >= 0:
                    blockedCharacters.add(res[i - j])
            for j in range(3):
                if chr(ord('a') + j) not in blockedCharacters:
                    res[i] = chr(ord('a') + j)
                    break
        return ''.join(res)

    def smallestBeautifulString(self, s: str, k: int) -> str:
        for index in range(len(s) - 1, -1, -1):
            seen = set()
            for j in range(1, 3):
                if index - j >= 0:
                    seen.add(s[index - j])
            for j in range(1, 4):
                if ord(s[index]) - ord('a') + j + 1 <= k and chr(ord(s[index]) + j) not in seen:
                    return self.generate(s, index, j)

