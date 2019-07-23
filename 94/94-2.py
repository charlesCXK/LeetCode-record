# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        if not root:
            return ret
        
        ret += self.inorderTraversal(root.left)
        ret.append(root.val)
        ret += self.inorderTraversal(root.right)
        
        return ret
        