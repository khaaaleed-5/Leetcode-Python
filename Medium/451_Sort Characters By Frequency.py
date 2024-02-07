from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counted_str = Counter(s)
        counted_str = sorted(zip(counted_str.values(), counted_str.keys()))
        ans = ''
        for i in counted_str[::-1]:
            ans += i[0] * i[1]

        return ans