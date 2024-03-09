class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        l1, r1 = 0, len(nums1)
        l2, r2 = 0, len(nums2)
        while l1 < r1 and l2 < r2:
            if nums1[l1] == nums2[l2]:
                return nums1[l1]
            else:
                if nums1[l1] < nums2[l2]:
                    l1 += 1
                elif nums1[l1] > nums2[l2]:
                    l2 += 1
        return -1