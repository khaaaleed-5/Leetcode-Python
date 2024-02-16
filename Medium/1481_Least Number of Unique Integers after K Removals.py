from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        rem = 0
        mp = Counter(arr)
        mp_values = sorted(mp.values())
        for i in mp_values:
            if k >= i:
                k -= i
                rem += 1
        return len(mp_values) - rem