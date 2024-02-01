"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        temp = root
        while temp and temp.left:
            temp2 = temp.left
            while temp:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                temp = temp.next
            temp = temp2
        return root
        