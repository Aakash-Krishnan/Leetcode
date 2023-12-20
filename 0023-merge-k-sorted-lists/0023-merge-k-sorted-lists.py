# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        
        newHead = tail = None
        if head1.val < head2.val:
            newHead = tail = head1
            head1 = head1.next
        else:
            newHead = tail = head2
            head2 = head2.next
        
        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            
            tail = tail.next
        
        if not head1:
            tail.next = head2
        if not head2:
            tail.next = head1
        
        return newHead
            

    def mergeSort(self, A, start, end):
        if start == end:
            return A[start]
        
        mid = start + (end - start) //2
        
        left = self.mergeSort(A, start, mid)
        right = self.mergeSort(A, mid + 1, end)
        
        return self.merge(left, right)
        
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.mergeSort(lists, 0, len(lists)-1)