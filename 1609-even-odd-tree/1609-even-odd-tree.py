# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        
        level = True
        while q:
            prevNode = float("-inf") if level else float("inf")
            for i in range(len(q)):
                node = q.popleft()
                if level and (node.val % 2 == 0 or prevNode >= node.val):
                        return False
                elif not level and (node.val % 2 or prevNode <= node.val):
                        return False
                    
                prevNode = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level = not level
        
        return True
                    