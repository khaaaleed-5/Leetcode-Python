class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        m = 0
        ans = 0
        happiness.sort()
        for i in range(len(happiness) - 1, -1, -1):
            if happiness[i] - m > 0 and k:
                ans += (happiness[i] - m)
            else:
                break
            m += 1
            k -= 1
        return ans     
