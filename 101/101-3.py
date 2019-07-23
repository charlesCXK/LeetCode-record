# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def checkMirror(root1, root2):
            if root1 == None:
                if root2 == None:
                    return True
                else:
                    return False
            if root2 == None:
                if root1 == None:
                    return True
                else:
                    return False    
            return checkMirror(root1.left, root2.right) and checkMirror(root1.right, root2.left) and root1.val==root2.val
        
        if not root:
            return True
        return checkMirror(root.left, root.right)