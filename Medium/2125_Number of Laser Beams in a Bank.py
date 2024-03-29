class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        one_1 = bank[0].count('1')
        for i in range(1, len(bank)):
            one_2 = bank[i].count('1')
            ans += (one_1 * one_2)
            if one_2 == 0:
                one_2 = one_1
            else:
                one_1 = one_2
        return ans