from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = defaultdict(list)
        for i in strs:
            sorted_word = ''.join(sorted(i))
            dict[sorted_word].append(i)
        ans = list(dict.values())
        return ans