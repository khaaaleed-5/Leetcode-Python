class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen =  [0] * 100
        ans = 0
        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            ans += seen[key]
            seen[key] += 1
        return ans
        
