class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = curr2 = head
        while curr and curr.next:
            curr,curr2 =curr.next.next,curr2.next
            if curr == curr2:
                return True 
        return False