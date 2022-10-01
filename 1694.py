class Solution:
    def reformatNumber(self, number: str) -> str:
        Chars = ""
        for num in number:
            if num != " " and num != "-":
                Chars += num
        Ans = ""
        if len(Chars) % 3 != 1:
            Index = 0
            while Index < len(Chars):
                if Index != 0 and Index % 3 == 0:
                    Ans += "-"
                Ans += Chars[Index]
                Index += 1
        else:
            Index = 0
            while Index < len(Chars):
                if Index != 0 and Index % 3 == 0:
                    Ans += "-"
                Ans += Chars[Index]
                if len(Chars) - Index == 4:
                    break
                Index += 1
            Index += 1
            Ans += Chars[Index]
            Index += 1
            Ans += "-"
            Ans += Chars[Index]
            Index += 1
            Ans += Chars[Index]
            Index += 1
        return Ans
