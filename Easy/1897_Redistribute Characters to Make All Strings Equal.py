from collections import Counter
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        mp = Counter()
        for i in words:
            mp.update(i)
        for i in mp.values():
            if i % len(words) != 0:
                return False
        return True