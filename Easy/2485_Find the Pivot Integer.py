class Solution:
    def pivotInteger(self, n: int) -> int:
        one_to_n = (n * (n + 1)) // 2
        for i in range(1, n + 1):
            one_to_x = (i * (i + 1)) // 2
            x_to_n = (one_to_n - one_to_x) + i
            if one_to_x == x_to_n:
                return i
        return -1
    
    '''
        Another Solution :
        
        nums = [i for i in range(1, n + 1)]
        s = (n * (n + 1)) // 2
        cs = 0
        for i in nums:
            cs += i
            if cs == s:
                return i
            s -= i
        return -1
        
    '''