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
        
        def checkOddLevel(val, prevVal, idx):
            if (val & 1):
                return False
            if not idx:
                return True
            if prevVal <= val:
                return False
            return True
            
        def checkEvenLevel(val, prevVal, idx):
            if not (val & 1):
                return False
            if not idx:
                return True
            if prevVal >= val:
                return False
            return True
        
        level = 0
        while q:
            prevNode = -1
            for i in range(len(q)):
                node = q.popleft()
                if (level & 1):
                    if not checkOddLevel(node.val, prevNode, i):
                        return False
                else:
                    if not checkEvenLevel(node.val, prevNode, i):
                        return False
                    
                prevNode = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level += 1
        
        return True
                    