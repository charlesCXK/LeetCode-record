'''
前序序列第一个是根节点。在中序序列中找到这个点的位置，左侧是左子树，右侧是右子树
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        # empty node
        if len(preorder) == 0:
            return None
        
        # find the index of root node in the inorder sequence
        root = preorder[0]
        rootindex = inorder.index(root)
        
        # length of left-tree and right-tree
        left_num, right_num = rootindex, len(inorder)-rootindex-1
        
        rootnode = TreeNode(root)       # this is root node
        rootnode.left = self.buildTree(preorder[1:1+left_num], inorder[0:left_num])
        rootnode.right = self.buildTree(preorder[1+left_num:], inorder[left_num+1:])
        
        return rootnode