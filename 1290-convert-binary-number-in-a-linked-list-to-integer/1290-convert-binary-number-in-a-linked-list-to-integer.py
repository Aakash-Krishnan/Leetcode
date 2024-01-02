# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        def reverse(head):
            curr = head
            prev = None
            while curr:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            
            return prev
        
        head = reverse(head)
        ans = 0
        pos = 0
        while head:
            ans += (head.val * (2**pos))
            head = head.next
            pos += 1
        return ans
            
        