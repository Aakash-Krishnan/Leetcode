# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head or not head.next and head.val == val:
            return None
        
        dummy = ListNode("dummy")
        tail = dummy
        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next
                head = head.next
            else:
                tail.next = head.next
                head.next = None
                head = tail.next
        
        return dummy.next
        
#         prev = temp = head
#         flag = False
        
#         while temp:
#             if temp.val == val:
#                 if temp == head:
#                     head = temp = prev = head.next   
#                 else:
#                     prev.next = temp.next
#                     temp.next = None
#                     temp = prev.next
#             else:
#                 temp = temp.next
#                 if flag:
#                     prev = prev.next
#                 else:
#                     flag = True
        
#         return head
            