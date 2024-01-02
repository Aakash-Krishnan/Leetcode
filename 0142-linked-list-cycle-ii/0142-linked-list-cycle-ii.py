# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = fast = head
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                flag = True
                break
        
        if flag:
            while True:
                if fast is head:
                    return head
                fast = fast.next
                head = head.next
                
        else:
            return None