'''
Runtime: 40 ms, faster than 97.87% of Python3 online submissions
Depth-First Search
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    paths = []
    
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        self.paths = []
        
        
        def dfs(root, path):
            if not root:
                return
            path.append(root.val)
            
            if not root.left and not root.right:
                self.paths.append(path)
                return
            if root.left:
                dfs(root.left, path.copy())
            if root.right:
                dfs(root.right, path.copy())
        
        dfs(root, [])
        
        # modify the format
        ret = []
        for path in self.paths:
            p = "" + str(path[0])
            for j in range(1, len(path)):
                p += "->"
                p += str(path[j])
            ret.append(p)
        return ret