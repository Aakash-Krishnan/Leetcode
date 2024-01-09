# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      
        def getLeaves(root):
            arr = []
            if not root.left and not root.right:
                arr.append(root.val)
            
            if root.left:
                arr += getLeaves(root.left)
            if root.right:
                arr += getLeaves(root.right)
            
            return arr
        
        
        
        return getLeaves(root1) == getLeaves(root2)