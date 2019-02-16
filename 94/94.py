# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    nodes = []
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.nodes.append(root.val)
            self.dfs(root.right)
        else:
            return
            
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        self.nodes = []
        self.dfs(root)
        return self.nodes
    