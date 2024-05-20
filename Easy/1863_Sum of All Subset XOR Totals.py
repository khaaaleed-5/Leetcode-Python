class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(number,total_numbers):
            if number == len(nums):
                return total_numbers
            
            return dfs(number + 1,total_numbers^nums[number]) + dfs(number + 1,total_numbers)
        
        return dfs(0,0)
