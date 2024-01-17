class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        frq = Counter(arr)
        return len(set(frq.values())) == len(frq.values())