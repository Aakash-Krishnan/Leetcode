# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        head = temp = node
        
        while temp:
            if temp.next:
                temp.val = temp.next.val
                if temp.next.next:
                    temp = temp.next
                else:
                    temp.next = None
                    break

        