# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def checkNextSet(head, k):
            while head and k:
                head = head.next
                k -= 1
            if head:
                return True
            return False
        
        def reverse(temp, k):
            curr = temp 
            prev = None
            while k:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
                k -= 1
            
            return curr, prev, temp
        
        temp = head
        newHead = None
        checker = head
        prevNode = None
        
        while temp:
            if checkNextSet(temp, k-1):
                temp, prev, end = reverse(temp, k)
                if not newHead:
                    newHead = prev
                
                end.next = temp
                if prevNode:
                    prevNode.next = prev
                prevNode = end
            
            else:
                break
        return newHead if newHead else head