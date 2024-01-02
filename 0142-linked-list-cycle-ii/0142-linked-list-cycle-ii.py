# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cache = {}
        pos = 0
        while head:
            if head in cache:
                return head
            cache[head] = pos
            head = head.next
            pos += 1
        
        return None