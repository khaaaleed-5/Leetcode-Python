class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt_one = s.count('1') - 1 
        ss = ""
        for i in range(len(s) - 1):
            if cnt_one:
                ss += '1'
                cnt_one -= 1
            else:
                ss += '0'

        ss += '1'
        return ss