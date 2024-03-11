from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        Sorted_String = ''
        mp = Counter(s)
        for i in s:
            if i not in order:
                Sorted_String += i

        for i in order:
            if i in s:
                Sorted_String += i * mp.get(i, 0)
        return Sorted_String