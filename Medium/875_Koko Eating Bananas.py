class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        if h == n:
            return max(piles)
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours_needed = sum((pile + mid - 1) // mid for pile in piles)
            if hours_needed > h:
                left = mid + 1
            else:
                right = mid
        return left