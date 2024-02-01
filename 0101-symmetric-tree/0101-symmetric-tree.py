# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(A, B):
            if not A and not B:
                return True
            elif not A or not B or A.val != B.val:
                return False
            
            return dfs(A.left, B.right) and dfs(A.right, B.left)
        
        return dfs(root.left, root.right)