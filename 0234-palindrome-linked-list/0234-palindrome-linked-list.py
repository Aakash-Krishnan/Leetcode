# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        h1 = head
        h2 = slow.next
        slow.next = None
        h2 = self.reverseList(h2)
        
        while h1 and h2:
            if h1.val != h2.val:
                return False
            
            h1 = h1.next
            h2 = h2.next
        
        return True
        