class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights1 = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != heights1[i]:
                ans += 1
        return ans
