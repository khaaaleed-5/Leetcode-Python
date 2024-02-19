class Solution:
    def maxArea(self, height: list[int]) -> int:
        elm = 0
        n = len(height)
        l, r = 0, n - 1
        while l <= r:
            w = r - l
            h = min(height[r], height[l])
            elm = max(w * h, elm)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return elm