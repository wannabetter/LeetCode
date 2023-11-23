def str2str(chars):
    if chars == "&quot;":
        return "\""
    elif chars == "&apos;":
        return '\''
    elif chars == "&amp;":
        return '&'
    elif chars == "&gt;":
        return ">"
    elif chars == "&lt;":
        return "<"
    elif chars == "&frasl;":
        return "/"
    else:
        return chars


def entityParser(text: str) -> str:
    ans = ""
    index, n = 0, len(text)
    while index < n:
        if text[index] == "&":
            chars = text[index]
            index = index + 1
            while index < n and text[index] not in ["&", ";"]:
                chars = chars + text[index]
                index = index + 1
            if index < n and text[index] == ";":
                chars = chars + text[index]
                index = index + 1
            ans = ans + str2str(chars)
        else:
            ans = ans + text[index]
            index = index + 1
    return ans













