# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {val: idx for idx, val in enumerate(inorder)}
        
        def tree(IL, IR, PL, PR):
            if IL > IR:
                return None
            
            node = TreeNode(preorder[PL])
            refIdx = cache[preorder[PL]]
            L = refIdx - IL
            node.left = tree(IL, refIdx - 1, PL + 1, PL + L)
            node.right = tree(refIdx + 1, IR, PL + L + 1, PR)
            
            return node
        
        return tree(0, len(inorder)-1 , 0, len(preorder)-1)