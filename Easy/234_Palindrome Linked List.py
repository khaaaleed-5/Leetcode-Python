class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        curr = head
        while curr:
            l += [curr.val]
            curr = curr.next
        return l == l[::-1]
        