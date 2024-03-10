class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        nums1 = [2,3,3,4]
        nums2 = [1,2,1,2,3]
        elements = set(nums1).intersection(nums2)
        return list(elements)
    
    '''
    Another Solution using difference:
    
        return list(set(nums1)-(set(nums1)-(set(nums2))))
    
    '''