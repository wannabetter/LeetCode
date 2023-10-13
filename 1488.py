from typing import List
from sortedcontainers import SortedList


def avoidFlood(rains: List[int]) -> List[int]:
    ans = [1] * len(rains)
    st = SortedList()
    mp = {}
    for index, rain in enumerate(rains):
        if rain == 0:
            st.add(index)
        else:
            ans[index] = -1
            if rain in mp:
                it = st.bisect(mp[rain])
                if it == len(st):
                    return []
                ans[st[it]] = rain
                st.discard(st[it])
            mp[rain] = index
    return ans