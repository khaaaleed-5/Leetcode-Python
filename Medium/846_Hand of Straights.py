class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        def find_group(hand, i, n):
            next_val = hand[i] + 1
            hand[i] = -1
            cnt = 1
            i += 1
            while i < len(hand) and cnt < n:
                if hand[i] == next_val:
                    next_val = hand[i] + 1
                    hand[i] = -1
                    cnt += 1
                i += 1
            return cnt == n

        if len(hand) % groupSize:
            return False
        hand.sort()
        for i in range(len(hand)):
            if hand[i] >= 0:
                if not find_group(hand,i,groupSize):
                    return False
        return True
        
