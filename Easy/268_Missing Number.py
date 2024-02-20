class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)
    
    """
    
    another soution : 
    
    nums.sort()
        n = len(nums)
        for i in range(n):
            if i != nums[i]:
                return i
        return n
        
    """
        
