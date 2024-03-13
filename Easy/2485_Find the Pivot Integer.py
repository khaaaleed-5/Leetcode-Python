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
        -----------------------------
        #1
        nums = [i for i in range(1, n + 1)]
        sum = (n * (n + 1)) // 2
        current = 0
        for i in nums:
            current += i
            if current == sum:
                return i
            sum -= i
        return -1
        -----------------------------
        #2
        x = sqrt(n * (n + 1) / 2)
        return int(x) if (x % 1) == 0 else -1
        
    '''