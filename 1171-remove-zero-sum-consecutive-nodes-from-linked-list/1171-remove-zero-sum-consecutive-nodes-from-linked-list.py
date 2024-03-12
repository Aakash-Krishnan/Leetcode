# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cache = {0: dummy}
        pSum = 0
        
        while head:
            pSum += head.val
            cache[pSum] = head
            head = head.next
        
        curr = dummy
        pSum = 0
        
        while curr:
            pSum += curr.val
            if pSum in cache:
                curr.next = cache[pSum].next
            curr = curr.next
        
        return dummy.next