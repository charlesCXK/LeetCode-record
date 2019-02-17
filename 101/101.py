# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # judge whether root1 and root2 are symmetric
    def judge(self, root1, root2):
        if not root1 and not root2:     # all empty
            return True
        elif (not root1) or (not root2):    # one is empty, the other is not
            return False
        elif root1.val != root2.val:
            return False
        
        symmetric1, symmetric2 = False, False
        if not root1.left and not root2.right:      # these two are empty
            symmetric1 = True
        elif root1.left and root2.right:
            symmetric1 = self.judge(root1.left, root2.right)
        
        if not root1.right and not root2.left:      # these two are empty
            symmetric2 = True
        elif root1.right and root2.left:
            symmetric2 = self.judge(root1.right, root2.left)
        return symmetric1 and symmetric2
        
        
        
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        # Recursively judge whether left of root and right of root are symmetric
        return self.judge(root.left, root.right)