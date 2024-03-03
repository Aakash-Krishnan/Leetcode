# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, A: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = A
        cnt = 1
        
        while fast:
            if cnt > n:
                if not fast.next:
                    slow.next = slow.next.next
                    return A
                else:
                    slow = slow.next
            fast = fast.next
            cnt += 1
        return A.next