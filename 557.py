def reverseWords(s: str) -> str:
    ans = ""
    for i in s.split(' '):
        i = i[::-1]
        ans = ans + i + " "
    return ans[:-1]


if __name__ == "__main__":
    reverseWords("Let's take LeetCode contest")
