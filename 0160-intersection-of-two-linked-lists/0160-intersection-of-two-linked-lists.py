# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = lenB = 0
        
        temp = headA
        while temp:
            lenA += 1
            temp = temp.next
        
        temp = headB
        while temp:
            lenB += 1
            temp = temp.next
        
        biggest, smallest = (headA, headB) if lenA > lenB else (headB, headA)
        lenDiff = abs(lenA - lenB)
        
        while lenDiff > 0:
            lenDiff -= 1
            biggest = biggest.next
        
        while biggest and smallest:
            if biggest == smallest:
                return biggest
            
            biggest = biggest.next
            smallest = smallest.next
        
        return None