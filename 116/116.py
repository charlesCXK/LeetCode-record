"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(root1, root2):
            if not root1:
                return
            root1.next = root2
            root.left.next = root.right
            
            dfs(root1.left, root1.right)        
            dfs(root2.left, root2.right)  
            dfs(root1.right, root2.left)    # Make up the middle gap
        
        if root:
            dfs(root.left, root.right)
        return root