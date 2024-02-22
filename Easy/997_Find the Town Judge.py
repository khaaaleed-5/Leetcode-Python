class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        mp = {}
        arr = [0] * (n + 1)
        if not trust:
            return n
        for i in trust:
            mp[i[1]] = mp.get(i[1], 0) + 1
            arr[i[0]] = 1
        for key, val in mp.items():
            if val == n - 1 and arr[key] == 0:
                return key
        return -1