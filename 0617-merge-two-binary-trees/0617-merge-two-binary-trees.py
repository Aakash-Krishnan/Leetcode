# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(A, B):
            if not A and not B:
                return None
            if not A:
                return B
            if not B:
                return A
            
            A.val += B.val
            A.left = dfs(A.left, B.left)
            A.right = dfs(A.right, B.right)
            return A
        
        return dfs(root1, root2)