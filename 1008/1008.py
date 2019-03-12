# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        root = TreeNode(preorder[0])
        
        target = len(preorder)
        for i,ele in enumerate(preorder):
            if ele > preorder[0]:
                target = i
                break
        root.left = self.bstFromPreorder(preorder[1:target])
        root.right = self.bstFromPreorder(preorder[target:])
        
        return root