# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = tail = None
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            Sum = v1 + v2 + carry
            carry = Sum // 10
            val = Sum % 10
            node = ListNode(val)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head