# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root):
        if not root:
            return ""
        
        if root.right:
            return str(root.val) + "(" + self.dfs(root.left) + ")(" + self.dfs(root.right) + ")"
        
        if root.left:
            return str(root.val) + "(" + self.dfs(root.left) + ")"
        
        return str(root.val)
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root)
    