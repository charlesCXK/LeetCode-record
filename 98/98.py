'''
64 ms
通过递归求二叉树最大最小值判断是否符合二叉搜索树的条件
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    valid = True
    
    def maxNode(self, root):
        # this BST has been proved to be invlalid
        if not self.valid:
            return -9999999999
        
        if not root.left and not root.right:
            return root.val
        
        left_max, right_max = -9999999999, -9999999999
        if root.left:
            left_max = max(left_max, self.maxNode(root.left))
            if left_max >= root.val:
                self.valid = False
        if root.right:
            right_max = max(right_max, self.maxNode(root.right))
            # if right_max <=root.val:
            #     self.valid = False
        
        return max(root.val, max(left_max, right_max))
    
    def minNode(self, root):
        # this BST has been proved to be invlalid
        if not self.valid:
            return 9999999999
        
        if not root.left and not root.right:
            return root.val
        
        left_min, right_min = 9999999999, 9999999999
        if root.left:
            left_min = min(left_min, self.minNode(root.left))
            # if left_min >= root.val:
            #     self.valid = False
        if root.right:
            right_min = min(right_min, self.minNode(root.right))
            if right_min <=root.val:
                self.valid = False
        
        return min(root.val, min(left_min, right_min))
            
            
            
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        self.valid = True
        
        # empty node
        if not root:
            return True
        
        max_val = self.maxNode(root)
        
        if self.valid:
            min_val = self.minNode(root)
        
        return self.valid