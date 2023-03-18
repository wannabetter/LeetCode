def checkPalindromeFormation(a: str, b: str) -> bool:
    def Check(str1, str2):
        left, right = 0, len(a) - 1
        while left < right and str1[left] == str2[right]:
            left += 1
            right -= 1
        s, t = str1[left:right+1], str2[left:right+1]
        return s == s[::-1] or t == t[::-1]

    return Check(a, b) or Check(b, a)
