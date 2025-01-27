class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for ls in matrix:
            l, r = 0, len(ls) - 1
            while l <= r:
                mid = (l + r) // 2
                if ls[mid] == target:
                    return True
                elif ls[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
