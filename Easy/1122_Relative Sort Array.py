class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        mp = Counter(arr1)
        for i in arr2:
            ans += [i] * mp[i]
            mp.pop(i)
        mp = sorted(zip(mp.keys(), mp.values()))
        for arr in mp:
            ans += [arr[0]] * arr[1]
        return ans
