# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      
        def getLeaves(root, leaves):
            if not root:
                return 
            if not root.left and not root.right:
                leaves.append(root.val)
                return 
            
            getLeaves(root.left, leaves)
            getLeaves(root.right, leaves)
        
        leaf1, leaf2 = [], []
        getLeaves(root1, leaf1)
        getLeaves(root2, leaf2)
        return leaf1 == leaf2