class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
    
    """
        another solution : 
        
        mp = Counter(nums)
        for i, j in mp.items():
            if j == 1:
                return i
                
    """
      