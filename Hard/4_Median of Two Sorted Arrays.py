import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        z = np.concatenate((nums1,nums2))
        z.sort()
        return round(np.median(z),4)