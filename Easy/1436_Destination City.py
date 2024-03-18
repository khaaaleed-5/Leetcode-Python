class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        mp = {}
        for i in paths:
            mp.update({i[0]: i[1]})
        for i in mp.values():
            if i not in mp.keys():
                return i
