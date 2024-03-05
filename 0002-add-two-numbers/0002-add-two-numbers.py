# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = tail = None
        
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            val %= 10
            node = ListNode(val)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = l1.val + carry
            carry = val // 10
            val %= 10
            node = ListNode(val)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            l1 = l1.next
        while l2:
            val = l2.val + carry
            carry = val // 10
            val %= 10
            node = ListNode(val)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            l2 = l2.next
        
        if carry:
            node = ListNode(carry)
            tail.next = node
        
        return head