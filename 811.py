from typing import List
from collections import Counter


def subdomainVisits(cpdomains: List[str]) -> List[str]:
    Res, Cnt = [], Counter()
    for cpdomain in cpdomains:
        Item, domain = cpdomain.split(" ")
        Item = int(Item)
        while len(domain) != 0:
            Cnt[domain] += Item
            Index = 0
            while Index < len(domain) and domain[Index] != '.':
                Index += 1
            domain = domain[Index + 1:]

    for Key in Cnt:

    return Res