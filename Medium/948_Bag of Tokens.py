class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        score = 0
        max_score = []
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        while l <= r:
            if tokens[l] > power:
                if score == 0:
                    break
                else:
                    power += tokens[r]
                    r -= 1
                    score -= 1
                    max_score += [score]
            elif tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
                max_score += [score]
        if not max_score:
            return score
        return max(max_score)