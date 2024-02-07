from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counted = Counter(s)
        for key,value in s_counted.items():
            if value == 1:
                return s.index(key)
        return -1