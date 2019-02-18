'''
Runtime: 220 ms, faster than 51.74% of Python3 online submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        # empty node
        if len(postorder) == 0:
            return None
        
        # find the index of root node in the inorder sequence
        root = postorder[-1]
        rootindex = inorder.index(root)
        
        # length of left-tree and right-tree
        left_num, right_num = rootindex, len(inorder)-rootindex-1
        
        rootnode = TreeNode(root)       # this is root node
        rootnode.left = self.buildTree(inorder[0:left_num], postorder[0:left_num])
        rootnode.right = self.buildTree(inorder[left_num+1:], postorder[left_num:-1])
        
        return rootnode
        